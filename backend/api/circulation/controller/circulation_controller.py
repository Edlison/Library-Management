# @Author  : Edlison
# @Date    : 12/31/20 18:32
from backend.api.circulation import cir_blu
from backend.filter.login_filter import need_login
from backend.api.circulation.service.circulation_service import borrow_book
from flask import request
# TODO 写接口和文档


@cir_blu.route('/borrow', methods=['POST'])
@need_login
def borrow():
    """
    借书流程：
    用户登陆 - 用户借书小于3本 - 库存大于1 - 库存减1 - 借阅表写入 - 用户借书数加1 - 借书成功
    Tips:
    默认借三个月

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:55
    """
    user_name = request.form.get('user_name')
    book_ISBN = request.form.get('book_ISBN')
    res = borrow_book(user_name, book_ISBN)



@cir_blu.route('/reserve', methods=['POST'])
@need_login
def reserve():
    """
    预约流程：
    用户登陆 - 用户预约数小于1 - 库存大于1 - 库存减1 - 预约表写入 - 用户预约数加1 - 预约成功

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:55
    """
    ...


@cir_blu.route('renew', methods=['POST'])
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
    ...


@cir_blu.route('/ret_book', methods=['POST'])
@need_login
def return_book():
    """
    还书流程：
    用户登陆 - 删借阅表信息 - 用户借阅数减1 - 还书成功

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 22:01
    """
    ...


@cir_blu.route('canc_resr', methods=['POST'])
@need_login
def cancel_reservation():
    """
    取消预约流程：
    用户登陆 - 删除预约表信息 - 用户预约数减1 - 取消成功

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 21:55
    """
    ...


@cir_blu.route('resr2borr')
@need_login
def reservation_to_borrowing():
    """
    预约改借阅：
    用户登陆 - 用户借书小于3本 - 删除预约表信息 - 用户预约数减1 - 增加借阅信息表信息 - 用户借阅数加1 - 预约改借阅成功

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/3/21 22:05
    """
    ...