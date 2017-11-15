#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 11:01
"""
from flask import make_response, request
from app import route
from msg import msg
from lib.utils.common import build_ret, err_ret, success_ret

from app.pretreatment.user_pretreat import login_pretreat, logout_pretreat


@route("/user/login", authentication=False, methods=['POST'])
def login():
    state, token = login_pretreat()
    if state:
        resp = success_ret(msg.LOGIN_SUCCESS)
        response = make_response(resp)
        response.headers['authorization'] = token
        return response
    else:
        return err_ret(msg.A_LOGIN_ERR)


@route("/user/logout", authentication=True, methods=['GET'])
def logout():
    token = request.headers.get('authorization')
    state = logout_pretreat(token)
    if state:
        return success_ret(msg.LOGOUT_SUCCESS)
    else:
        return err_ret(msg.A_TIMEOUT)
