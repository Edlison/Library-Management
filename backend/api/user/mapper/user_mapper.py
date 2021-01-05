# @Author  : Edlison
# @Date    : 1/3/21 09:48
from backend.api.user.models.user_model import User
from backend.api import db
from sqlalchemy import and_
import datetime
from hashlib import sha256


def get_user_by_name_password(user_name, user_password):
    """
    通过用户和密码获取用户

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:00
    """
    user = User.query.filter(and_(User.user_name==user_name, User.user_password==user_password)).first()
    return user


def update_user_login_time(user_name):
    """
    用户登陆更新登陆时间

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:00
    """
    p = User.query.filter(User.user_name==user_name).update({'user_last_login_time': datetime.datetime.now()})
    db.session.commit()


def get_user_by_name(user_name):
    """
    通过user_name获取用户

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:01
    """
    user = User.query.filter_by(user_name=user_name).first()
    return user


def add_user_borrowing(user_name):
    """
    用户增加借阅数量

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:01
    """
    user = User.query.filter_by(user_name=user_name).first()
    user.user_borrowing += 1
    db.session.commit()

def reduce_user_borrowing(user_name):
    """
    用户减少借阅数量

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:01
    """
    user = User.query.filter_by(user_name=user_name).first()
    user.user_borrowing -= 1
    db.session.commit()


def add_user_reser(user_name):
    """
    用户增加预约数量

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:02
    """
    user = User.query.filter_by(user_name=user_name).first()
    user.user_reserving += 1
    db.session.commit()


def reduce_user_reser(user_name):
    """
    用户减少预约数量

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:02
    """
    user = User.query.filter_by(user_name=user_name).first()
    user.user_reserving -= 1
    db.session.commit()


def insert_user(user_name, user_password, user_role):
    """
    关闭
    录入用户

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 17:02
    """
    user = User(user_name, sha256(user_password.encode('utf-8')).hexdigest(), user_role, datetime.datetime.now())
    db.session.add(user)
    db.session.commit()
