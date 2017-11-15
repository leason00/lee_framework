#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/15 14:13
"""
from app.utils.get_info import get_params, get_user_info
from app.utils.opreate_token import en_token
from conf import redis_pre
from db import redis_conn as redis_server

from app.services.user_service import login_service


def login_pretreat():
    """
    登录处理
    :return:state, token
    """
    params = get_params()
    state, result = login_service(params['username'])
    if state:
        if result["password"] == params['password']:
            token = en_token(username=params['username'])
            redis_server.set(redis_pre['token_pix'] + params['username'], token)
            return True, token

    return False, None


def logout_pretreat(token):
    """

    :param token:
    :return:
    """
    redis_server.delete(token)
    username = get_user_info()['username']
    redis_server.delete(redis_pre['token_pix'] + username)

    return True