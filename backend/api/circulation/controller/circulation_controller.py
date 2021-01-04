# @Author  : Edlison
# @Date    : 12/31/20 18:32
from backend.api.circulation import cir_blu
from backend.filter.login_filter import need_login
from backend.api.circulation.service.circulation_service import \
    borrow_book, reser_book, get_borrow_books, get_resr_book, get_certain_book, get_all_books, renew_book, return_book, \
    cancel_resr, resr_to_borrow
from flask import request, jsonify, session


@cir_blu.route('/borrow', methods=['POST'])
@need_login
def borrow():  # TODO 完善borrow 1. catlog表（isbn主键 图书余量字段） 2. 添加借阅信息的datetime
    """
    借书流程：
    用户登陆 - 用户借书小于3本 - 库存大于1 - 库存减1 - 借阅表写入 - 用户借书数加1 - 借书成功
    Tips:
    默认借3个月

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:55
    """
    user_name = session.get('user_name')
    book_ISBN = request.form.get('book_ISBN')
    res = borrow_book(user_name, book_ISBN)
    return jsonify(dict(res))


@cir_blu.route('/reserve', methods=['POST'])
@need_login
def reserve():
    """
    预约流程：
    用户登陆 - 用户预约数小于1 - 库存大于1 - 库存减1 - 预约表写入 - 用户预约数加1 - 预约成功
    Tips:
    默认预约3个月

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:55
    """
    user_name = session.get('user_name')
    book_ISBN = request.form.get('book_ISBN')
    res = reser_book(user_name, book_ISBN)
    return jsonify(dict(res))


@cir_blu.route('/get_borrow', methods=['POST'])
@need_login
def get_borrow():
    """
    获取用户借阅信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 14:40
    """
    user_name = session.get('user_name')
    res = get_borrow_books(user_name)
    return jsonify(dict(res))


@cir_blu.route('/get_resr', methods=['POST'])
@need_login
def get_resr():
    """
    获取用户预约信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 14:40
    """
    user_name = session.get('user_name')
    res = get_resr_book(user_name)
    return jsonify(dict(res))


@cir_blu.route('/renew', methods=['POST'])
@need_login
def renew():
    """
    续借流程：
    用户登陆 - 续借剩余次数大于0 - 应还日期加1月 - 续借次数减1 - 续借成功

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 22:24
    """
    borrow_id = request.form.get('borrow_id')
    res = renew_book(borrow_id)
    return jsonify(dict(res))


@cir_blu.route('/ret_book', methods=['POST'])
@need_login
def return_():
    """
    还书流程：
    用户登陆 - 删借阅表信息 - 用户借阅数减1 - 库存加1 - 还书成功

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 22:01
    """
    user_name = session.get('user_name')
    borrow_id = request.form.get('borrow_id')
    res = return_book(user_name, borrow_id)
    return jsonify(dict(res))


@cir_blu.route('/canc_resr', methods=['POST'])
@need_login
def cancel():
    """
    取消预约流程：
    用户登陆 - 删除预约表信息 - 用户预约数减1 - 库存加1 - 取消成功

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:55
    """
    user_name = session.get('user_name')
    reser_id = request.form.get('reser_id')
    res = cancel_resr(user_name, reser_id)
    return jsonify(dict(res))


@cir_blu.route('/resr2borr', methods=['POST'])
@need_login
def resr2borr():
    """
    预约改借阅：
    用户登陆 - 用户借书小于3本 - 删除预约表信息 - 用户预约数减1 - 增加借阅信息表信息 - 用户借阅数加1 - 预约改借阅成功

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 22:05
    """
    user_name = session.get('user_name')
    reser_id = request.form.get('reser_id')
    res = resr_to_borrow(user_name, reser_id)
    return jsonify(dict(res))


@cir_blu.route('/get_book', methods=['POST'])
@need_login
def get_book():
    """
    获取图书详细信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 14:41
    """
    book_ISBN = request.form.get('book_ISBN')
    res = get_certain_book(book_ISBN)
    return jsonify(dict(res))


@cir_blu.route('/get_all_books', methods=['POST'])
@need_login
def all():
    """
    获取馆藏信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 14:42
    """
    res = get_all_books()
    return jsonify(dict(res))
