# @Author  : Edlison
# @Date    : 12/29/20 01:41
from backend.api import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(32), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    user_role = db.Column(db.Integer, nullable=False)
    user_borrowing = db.Column(db.Integer, nullable=True)
    user_reserving = db.Column(db.Integer, nullable=True)
    user_credit = db.Column(db.Integer, nullable=True)
    user_create_time = db.Column(db.DateTime, nullable=True)
    user_last_login_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_name, user_password, user_role):
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role

    def keys(self):
        return ['user_name', 'user_role', 'user_borrowing', 'user_reserving', 'user_credit', 'user_last_login_time']

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return '<User user_name: {}>'.format(self.user_name)
