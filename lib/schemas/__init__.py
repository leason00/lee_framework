# encoding: utf-8

"""
@version: 1.0
@author: dawning
@contact: dawning7670@gmail.com
@time: 2017/3/29 15:20
"""
from app_config import schema_config as app_schema_config
from app_request import schema_config as app_schema_request
from lib.utils import package_import

package_import("lib.schemas", excludes=["example_schema"])
package_import("schemas", excludes=["example_schema"])
