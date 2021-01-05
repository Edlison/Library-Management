# @Author  : Edlison
# @Date    : 12/28/20 18:10
from backend.api.user import user_blu
from flask import request, jsonify, session, g
from backend.filter.login_filter import need_login
from backend.result.system_result import SystemResult
from backend.util.serialize import serialize_model
from backend.api.user.service.user_service import validate, info, exceed_the_time, register, get_user_all,\
    change_password, delete_user


@user_blu.route('/register', methods=['POST'])
@need_login
def r():
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
    res = register(user_name, user_password, user_role)
    return jsonify(dict(res))


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


@user_blu.route('/change_password', methods=['POST'])
@need_login
def repasword():
    user_id = request.form.get('user_id')
    user_new_password = request.form.get('user_new_password')
    res = change_password(user_id, user_new_password)
    return jsonify(dict(res))


@user_blu.route('/delete_user', methods=['POST'])
@need_login
def du():
    user_id = request.form.get('user_id')
    if int(user_id) == int(session.get('user_id')):
        return jsonify(dict(SystemResult().error('不能删除本账号')))
    res = delete_user(user_id)
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


@user_blu.route('/get_user_all', methods=['POST'])
@need_login
def gua():
    res = get_user_all()
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
