#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/15 14:32
"""
from sqlalchemy import Column, Integer, String, Enum, DateTime
from db.mysql.mysql_pool import ModelBase
from lib.utils.common import date_time


# 个体用户表
class User(ModelBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)              # id
    create_time = Column(DateTime, default="")                              # 创建时间
    telephone = Column(String(length=15), default="")                       # 绑定手机号
    password = Column(String(length=50), default="")                        # 登录密码
    username = Column(String(length=20), default="", unique=True)           # 昵称
    enable = Column(Enum(*("0", "1")), default="0")                         # 状态  0：启用、1：禁用

    def __init__(self, username, password, telephone=None):
        self.create_time = date_time()
        self.username = username
        self.password = password
        self.telephone = telephone

    def to_json(self):
        return {
            "username": self.username,
            "telephone": self.telephone,
            "create_time": self.create_time
        }
