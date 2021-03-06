# @Author  : Edlison
# @Date    : 1/3/21 09:41
from backend.api.user.mapper.user_mapper import get_user_by_name_password, update_user_login_time, get_user_by_name, \
    insert_user, get_all, get_user_by_id, update_user_pwd_by_id, delete_user_by_id
from backend.api.circulation.mapper.circulation_mapper import get_borrowing_books_by_user_name, get_book_by_isbn
from backend.result.system_result import SystemResult
from hashlib import sha256
from flask import g
import datetime
from backend.util.datetime_cmp import is_dt_later
from backend.util.serialize import serialize_model_list


def register(user_name, user_password, user_role):
    user = get_user_by_name(user_name)
    res = SystemResult()
    if not user:
        insert_user(user_name, user_password, user_role)
        res.ok('插入用户成功')
    else:
        res.error('已有该用户')
    return res


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
        g.user_role = user.user_role
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


def get_user_all():
    """
    获取所有用户列表

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/5/21 16:33
    """
    users = get_all()
    res = SystemResult()
    if users and len(users) > 0:
        res.set_data(serialize_model_list(users))
        res.ok('获取用户列表成功')
    else:
        res.error('没有用户')
    return res


def change_password(user_id, user_new_password):
    user = get_user_by_id(user_id)
    res = SystemResult()
    if user:
        encoded_pwd = sha256(user_new_password.encode('utf-8')).hexdigest()
        if user.user_password != encoded_pwd:
            row = update_user_pwd_by_id(user_id, encoded_pwd)
            if row > 0:
                res.ok('修改成功')
            else:
                res.error('修改失败')
        else:
            res.error('密码不能与上一个相同')
    else:
        res.error('没有这个用户')
    return res


def delete_user(user_id):
    user = get_user_by_id(user_id)
    res = SystemResult()
    if user:
        if user.user_borrowing == 0 and user.user_reserving == 0:
            row = delete_user_by_id(user_id)
            if row > 0:
                res.ok('删除成功')
            else:
                res.error('删除失败')
        else:
            res.error('用户不能有书在流通')
    else:
        res.error('没有这个用户')
    return res


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
        data = serialize_model_list(data)
        for d in data:  # 获取每本书名
            book_detail = get_book_by_isbn(d['borrow_book_isbn'])
            d['borrow_book_name'] = book_detail.book_name
        res.set_data(data)
        res.ok('获取超期图书成功')
    else:
        res.error('没有该用户的图书信息')
    return res
