#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 9:55
"""

from lib.schemas import app_schema_request


app_schema_request['/test'] = {
    'name': {'type': 'string'},
    'enable': {'type': 'string', 'enum': ['0', '1']}
}