#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/15 15:07
"""
from flask import g
from app.models.user_models import User
from app.utils.get_info import get_session


@get_session
def login_service(username):
    """
    登录
    :param username:
    :return:
    """
    session = g.session
    username, password = session.query(User.username, User.password).filter(User.username == username).one_or_none()
    result = dict()
    if username is not None:
        result['username'] = username
        result['password'] = password
        return True, result

    return False, result