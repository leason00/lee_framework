#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 11:01
"""
from app import route


@route("/test", methods=['POST'])
def test():
    print 8888
    return '888'