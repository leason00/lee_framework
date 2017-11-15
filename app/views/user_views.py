#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 11:01
"""
from flask import make_response
from app import route
from msg import msg
from lib.utils.common import build_ret, err_ret, success_ret

from app.pretreatment.user_pretreat import login_pretreat


@route("/user/login", authentication=False, methods=['POST'])
def login():
    state, token = login_pretreat()
    if state:
        resp = success_ret(msg.SUCCESS, msg="登录成功！")
        response = make_response(resp)
        response.headers['authorization'] = token
        return response
    else:
        return err_ret(msg.A_LOGIN_ERR)
