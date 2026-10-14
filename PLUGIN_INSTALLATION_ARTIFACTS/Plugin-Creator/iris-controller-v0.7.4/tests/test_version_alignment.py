import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_manifest_versions_aligned():
    assert json.loads((ROOT / 'plugin.json').read_text())['version'] == '0.7.4'
    assert json.loads((ROOT / '.codex-plugin/plugin.json').read_text())['version'] == '0.7.4'

def test_active_mcp_entrypoint_is_merged_and_version_aligned():
    config = json.loads((ROOT / '.mcp.json').read_text())
    assert config['mcpServers']['iris-controller']['args'] == ['runtime/launch_merged_mcp.py']
    source = (ROOT / 'runtime/merged_mcp_server.py').read_text()
    assert "APP_VERSION='0.7.4'" in source
    assert 'base.APP_VERSION = APP_VERSION' in source

def test_legacy_rest_runtime_is_explicitly_separate():
    source = (ROOT / 'runtime/main.py').read_text()
    assert 'APP_VERSION = "0.6.19"' in source
