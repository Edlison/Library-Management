# @Author  : Edlison
# @Date    : 12/29/20 01:41
from backend.api import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(32), unique=True)
    user_password = db.Column(db.String(32), unique=True)
    user_role = db.Column(db.Integer)
    user_credit = db.Column(db.Integer)
    user_create_time = db.Column(db.Date)
    user_last_login_time = db.Column(db.Date)

    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password

    def set_role(self, role):
        self.user_role = role

    def keys(self):
        return ['user_id', 'user_name']

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return '<User user_name: {}, user_password: {}>'.format(self.user_name, self.user_password)


class Role(db.Model):
    __tablename__ = 'role'
    role_id = db.Column(db.Integer, primary_key=True)
    role_rights = db.Column(db.String(10))