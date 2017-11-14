#!/usr/bin/env python
# encoding: utf-8
"""
@author: leason
@time: 2017/11/14 9:54
"""
ENVIRONMENT = False
if ENVIRONMENT:
    from ConfigService.online_config import *
else:
    from ConfigService.local_config import *