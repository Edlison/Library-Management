# @Author  : Edlison
# @Date    : 1/3/21 09:41
from backend.api.user.mapper.user_mapper import get_user_by_name_password, update_user_login_time, get_user_by_name
from backend.result.system_result import SystemResult
from hashlib import sha256
from flask import g


def validate(user_name, user_password):
    user = get_user_by_name_password(user_name, sha256(user_password.encode('utf-8')).hexdigest())
    if user:
        g.user_id = user.user_id
        update_user_login_time(user_name)
        res = SystemResult().ok()
    else:
        res = SystemResult().error()
    return res


def info(user_name):
    user = get_user_by_name(user_name)
    return user

