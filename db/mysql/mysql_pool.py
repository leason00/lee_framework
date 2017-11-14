#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 14:35
"""
from sqlalchemy import create_engine, exc
from sqlalchemy.pool import QueuePool
from lib.utils import logging
from conf import mysql_pool_configs


def engine():
    db_pool = None
    try:
        db_pool = create_engine(mysql_pool_configs['url'], poolclass=QueuePool,
                                pool_size=mysql_pool_configs['pool_size'],
                                max_overflow=mysql_pool_configs['max_overflow'],
                                pool_recycle=mysql_pool_configs['pool_recycle'],
                                echo=True
                                )
    except exc.OperationalError as e:
        logging.debug("create pool err:", e)
    return db_pool
mysql_engine = engine()
