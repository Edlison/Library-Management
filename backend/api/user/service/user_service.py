# @Author  : Edlison
# @Date    : 1/3/21 09:41
from backend.api.user.mapper.user_mapper import get_user_by_name_password, update_user_login_time, get_user_by_name
from backend.api.circulation.mapper.circulation_mapper import get_borrowing_books_by_user_name
from backend.result.system_result import SystemResult
from hashlib import sha256
from flask import g
import datetime
from backend.util.datetime_cmp import is_dt_later
from backend.util.serialize import serialize_model_list


def validate(user_name, user_password):
    """
    密码验证逻辑

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:59
    """
    user = get_user_by_name_password(user_name, sha256(user_password.encode('utf-8')).hexdigest())
    if user:
        g.user_id = user.user_id
        update_user_login_time(user_name)
        res = SystemResult().ok()
    else:
        res = SystemResult().error()
    return res


def info(user_name):
    """
    获取用户信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:00
    """
    user = get_user_by_name(user_name)
    return user


def exceed_the_time(user_name):
    """
    超期提醒逻辑

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:38
    """
    books = get_borrowing_books_by_user_name(user_name)
    res = SystemResult()
    if books is not None:
        now = datetime.datetime.now()
        data = []
        for book in books:
            if is_dt_later(now, book.borrow_end_time):
                data.append(book)
        res.set_data(serialize_model_list(data))
        res.ok('获取超期图书成功')
    else:
        res.error('没有该用户的图书信息')
    return res
