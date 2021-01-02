# @Author  : Edlison
# @Date    : 12/28/20 18:10
from backend.api.user import user_blu
from flask import request, jsonify, session
from backend.filter.login_filter import need_login
from backend.api.user.models.user_model import User
from backend.result.system_result import SystemResult
from backend.util.serialize import serialize_model_list


@user_blu.route('/login', methods=['POST'])
def login():
    user_name = request.form['user_name']
    session['user_name'] = user_name
    res = SystemResult().ok()
    res.set_data(user_name)
    return jsonify(dict(res))


@user_blu.route('/get_info', methods=['POST'])
@need_login
def get_info():
    user_name = session.get('user_name')
    if user_name:
        users = User.query.filter_by(user_name=user_name).all()
        if users and len(users) == 1:
            res = SystemResult().ok()
            res.set_data(serialize_model_list(users))
            return jsonify(dict(res))
        else:
            res = SystemResult().error('找到多个用户')
            res.set_data(dict(users))
            return jsonify(dict(res))
    else:
        res = SystemResult().error('未找到用户')
        return jsonify(dict(res))
