#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 9:54
"""
from lib.flask import app


@app.teardown_request
def teardown_request(exception):
    pass

