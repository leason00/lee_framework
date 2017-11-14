# encoding: utf-8

"""
@author: leason
@time: 2017/11/14 9:59
"""
from conf import web
from lib.flask import app

# 需要登录的接口
login_list = []


# route装饰器
# 处理app.route装饰的方法名称相同的情况
def route(rule, authentication=False, **options):
    def wrapper(func):
        options['endpoint'] = rule
        # 处理多版本api
        for rl in make_rule(web['url_pre'], web['api_version'], rule):
            if authentication:
                login_list.append(rl)
            app.route(rl, **options)(func)
        return wrapper

    return wrapper


def make_rule(prefix, api_vers, rule):
    if not prefix.endswith("/"):
        prefix += "/"
    return [prefix + api + rule for api in api_vers]
