# @Author  : Edlison
# @Date    : 12/28/20 18:10
from backend.api.user import user_blu
from flask import request, jsonify, session, g
from backend.filter.login_filter import need_login
from backend.result.system_result import SystemResult
from backend.util.serialize import serialize_model_list, serialize_model
from backend.api.user.service.user_service import validate, info


@user_blu.route('/register', methods=['POST'])
def register():
    ...


@user_blu.route('/login', methods=['POST'])
def login():
    """
    用户登陆

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:51
    """
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    res = validate(user_name, user_password)
    if res.is_ok():
        session['user_name'] = user_name
        session['user_id'] = g.user_id
        res.ok('登陆成功')
    else:
        res.error('账号或密码错误')
    return jsonify(dict(res))


@user_blu.route('/get_info', methods=['POST'])
@need_login
def get_info():
    """
    获取用户信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:52
    """
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


@user_blu.route('/exceed_the_time', methods=['POST'])
@need_login
def exceed_the_time():  # TODO 超期提醒
    """
    超期提醒
    用last_login去比对

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:52
    """
    ...