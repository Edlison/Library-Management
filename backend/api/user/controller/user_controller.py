# @Author  : Edlison
# @Date    : 12/28/20 18:10
from backend.api.user import user_blu
from flask import request, jsonify, session, g
from backend.filter.login_filter import need_login
from backend.result.system_result import SystemResult
from backend.util.serialize import serialize_model_list, serialize_model
from backend.api.user.service.user_service import validate, info, exceed_the_time
from backend.api.user.mapper.user_mapper import insert_user


@user_blu.route('/register', methods=['POST'])
@need_login
def register():  # TODO 完善注册 1. 用户名密码合法性判断 2. 查重复用户
    """
    关闭
    注册接口

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:59
    """
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_password')
    user_role = request.form.get('user_role')
    insert_user(user_name, user_password, user_role)
    return 'ok'


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
        res.set_data({'user_role': g.user_role})
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
def exceed():
    """
    超期提醒
    用last_login去比对

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:52
    """
    user_name = session.get('user_name')
    res = exceed_the_time(user_name)
    return jsonify(dict(res))
