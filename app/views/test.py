#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 11:01
"""
from app import route


@route("/test", authentication=False, methods=['POST'])
def test():
    return '888'