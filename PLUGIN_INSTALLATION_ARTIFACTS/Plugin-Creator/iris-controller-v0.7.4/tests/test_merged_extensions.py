"""Regression tests for merged usage ledger and deterministic project policy."""
import sys, tempfile, uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'runtime'))
import database
import merged_extensions as ext
from controller import create_work


def setup_db(monkeypatch):
    path = Path(tempfile.mkdtemp()) / 'merged-test.db'
    monkeypatch.setenv('IRIS_DB_PATH', str(path))
    database.set_db_path(path)
    ext.init_extensions()


def test_usage_create_list_update_audit(monkeypatch):
    setup_db(monkeypatch)
    created = ext.usage_record({'category':'api','action':'calls','value':3,'unit':'calls','source':'test'})
    uid = created['usage_id']
    assert created['value'] == 3
    assert ext.usage_list({'category':'api'})['count'] == 1
    updated = ext.usage_update({'usage_id':uid,'updates':{'value':4,'status':'VERIFIED'}})
    assert updated['value'] == 4 and updated['status'] == 'VERIFIED'
    assert [x['event'] for x in updated['audit']] == ['CREATED','UPDATED']


def test_project_policy_blocks_budget_and_duplicate(monkeypatch):
    setup_db(monkeypatch)
    p = ext.create_project({'name':'test project','budget_limit':5,'allowed_phases':['MCR','SRR']})
    assert ext.check_project_policy({'project_id':p['project_id'],'phase':'MCR','budget_amount':4})['passed'] is True
    assert 'BUDGET_EXCEEDED' in ext.check_project_policy({'project_id':p['project_id'],'phase':'MCR','budget_amount':6})['errors']
    task = ext.create_controlled_task({'project_id':p['project_id'],'title':'first task','phase':'MCR','budget_amount':2}, type('Base',(),{'create_work':staticmethod(create_work)})())
    assert task['status'] == 'PENDING'
    duplicate = ext.check_project_policy({'project_id':p['project_id'],'title':'first task','phase':'MCR','budget_amount':0})
    assert 'DUPLICATE_TASK' in duplicate['errors']


def test_project_policy_blocks_invalid_phase(monkeypatch):
    setup_db(monkeypatch)
    p = ext.create_project({'name':'phase project','allowed_phases':['MCR']})
    result = ext.check_project_policy({'project_id':p['project_id'],'phase':'ORR'})
    assert result['passed'] is False and 'PHASE_NOT_ALLOWED' in result['errors']
