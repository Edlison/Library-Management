# @Author  : Edlison
# @Date    : 12/28/20 18:10
from backend.api.user import user_blu
from flask import request, jsonify, session
from backend.filter.login_filter import need_login
from backend.api.user.models.user_model import User
from backend.result.system_result import SystemResult
from backend.util.serialize import serialize_model_list, serialize_model
from backend.api.user.service.user_service import validate, info


@user_blu.route('/register', methods=['POST'])
def register():
    ...


@user_blu.route('/login', methods=['POST'])
def login():
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    res = validate(user_name, user_password)
    if res.is_ok():
        session['user_name'] = user_name
        res.ok('登陆成功')
    else:
        res.error('账号或密码错误')
    return jsonify(dict(res))


@user_blu.route('/get_info', methods=['POST'])
@need_login
def get_info():
    user_name = session.get('user_name')
    if user_name:
        user = info(user_name)
        if user:
            res = SystemResult().ok()
            res.set_data(serialize_model(user))
            return jsonify(dict(res))
    else:
        res = SystemResult().error('未找到用户')
        return jsonify(dict(res))
