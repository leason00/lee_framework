#!/usr/bin/env python
# encoding: utf-8
'''
@author: WL
@time: 2017/10/19 15:44
'''
from lib.schemas import app_schema_request


app_schema_request['/admin/role/new'] = {
    'name': {'type': 'string'},
    'enable': {'type': 'string', 'enum': ['0', '1']}
}


app_schema_request['/admin/role/delete'] = {
    'id': {'type': 'string','pattern':'^[1-9]\d*$'}
}

app_schema_request['/admin/role/edit'] = {
    'id': {'type': 'string','pattern':'^[1-9]\d*$'},
    'name': {'type': 'string'},
    'enable': {'type': 'string', 'enum': ['0', '1']}
}

app_schema_request['/admin/role'] = {
    'limit': {'type': 'integer'},
    'page': {'type': 'integer'}
}