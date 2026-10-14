"""Unified IRIS MCP entrypoint: core controller + usage ledger + project policy."""
import asyncio, json, sys, uuid
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import database
import mcp_server as base
import merged_extensions as ext
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

APP_VERSION='0.7.4'
base.APP_VERSION = APP_VERSION
server=Server('iris-controller')
EXTRA_TOOLS=[
 Tool(name='create_project',description='Create a project with deterministic budget and phase controls.',inputSchema={'type':'object','properties':{'project_id':{'type':'string'},'name':{'type':'string'},'budget_limit':{'type':['number','null']},'current_phase':{'type':'string'},'allowed_phases':{'type':'array','items':{'type':'string'}}},'required':['name']}),
 Tool(name='check_project_policy',description='Check project status, phase, budget, and duplicate-task constraints without executing.',inputSchema={'type':'object','properties':{'project_id':{'type':'string'},'phase':{'type':'string'},'budget_amount':{'type':'number'},'title':{'type':'string'},'allow_rerun':{'type':'boolean'}},'required':['project_id']}),
 Tool(name='create_controlled_task',description='Create a task only after deterministic project, phase, budget, and duplicate-task policy passes.',inputSchema={'type':'object','properties':{'project_id':{'type':'string'},'title':{'type':'string'},'phase':{'type':'string'},'budget_amount':{'type':'number'},'work_id':{'type':'string'},'task_id':{'type':'string'},'assignee':{'type':'string'},'allow_rerun':{'type':'boolean'}},'required':['project_id','title']}),
 Tool(name='record_usage',description='Persist a usage ledger record with generated ID, timestamps, and audit history.',inputSchema={'type':'object','properties':{'category':{'type':'string'},'action':{'type':'string'},'value':{},'unit':{'type':'string'},'source':{'type':'string'},'status':{'type':'string'},'notes':{'type':'string'}},'required':['category','action','value']}),
 Tool(name='list_usage',description='List usage records, optionally filtered by category or status.',inputSchema={'type':'object','properties':{'category':{'type':'string'},'status':{'type':'string'}}}),
 Tool(name='get_usage',description='Read one usage record and its audit history by exact ID.',inputSchema={'type':'object','properties':{'usage_id':{'type':'string'}},'required':['usage_id']}),
 Tool(name='update_usage',description='Update a usage record by exact ID and append an audit entry.',inputSchema={'type':'object','properties':{'usage_id':{'type':'string'},'updates':{'type':'object'}},'required':['usage_id','updates']}),
]

def reply(data): return [TextContent(type='text',text=json.dumps(data,ensure_ascii=False,default=str))]

@server.list_tools()
async def list_tools(): return list(base.TOOLS)+EXTRA_TOOLS

@server.call_tool()
async def call_tool(name:str,arguments:dict):
    ext.init_extensions()
    a=arguments or {}
    try:
        if name=='create_project': return reply({'status':'OK','version':APP_VERSION,**ext.create_project(a)})
        if name=='check_project_policy': return reply({'status':'OK','version':APP_VERSION,**ext.check_project_policy(a)})
        if name=='create_controlled_task': return reply({'status':'OK','version':APP_VERSION,**ext.create_controlled_task(a,base)})
        if name=='record_usage': return reply({'status':'OK','version':APP_VERSION,'record':ext.usage_record(a)})
        if name=='list_usage': return reply({'status':'OK','version':APP_VERSION,**ext.usage_list(a)})
        if name=='get_usage': return reply({'status':'OK','version':APP_VERSION,'record':ext.usage_get(a)})
        if name=='update_usage': return reply({'status':'OK','version':APP_VERSION,'record':ext.usage_update(a)})
        return await base.call_tool(name,a)
    except ValueError as exc:
        return reply({'status':'ERROR','error_type':'POLICY_OR_VALIDATION','message':str(exc),'version':APP_VERSION})
    except Exception as exc:
        return reply({'status':'ERROR','error_type':'INTERNAL','message':f'{type(exc).__name__}: {exc}','version':APP_VERSION})

async def main():
    ext.init_extensions()
    async with stdio_server() as (reader,writer):
        await server.run(reader,writer,server.create_initialization_options())
