# @Author  : Edlison
# @Date    : 1/3/21 09:48
from backend.api.user.models.user_model import User
from backend.api import db
from sqlalchemy import and_
import datetime


def get_user_by_name_password(user_name, user_password):
    user = User.query.filter(and_(User.user_name==user_name, User.user_password==user_password)).first()
    return user


def update_user_login_time(user_name):
    p = User.query.filter(User.user_name==user_name).update({'user_last_login_time': datetime.datetime.now().timestamp()})
    db.session.commit()


def get_user_by_name(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    return user


def update_user_borrowing(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    user.user_borrowing += 1
    db.session.commit()
