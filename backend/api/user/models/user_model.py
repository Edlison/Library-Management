# @Author  : Edlison
# @Date    : 12/29/20 01:41
from backend.api import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    user_name = db.Column(db.String(32), unique=True, nullable=False, comment='用户名')
    user_password = db.Column(db.String(255), nullable=False, comment='密码')
    user_role = db.Column(db.Integer, nullable=False, default=1, comment='用户角色 0superadmin/1reader/2inter/3cat/4cir/5useradmin')
    user_borrowing = db.Column(db.Integer, nullable=True, default=0, comment='借书不能超过3本')
    user_reserving = db.Column(db.Integer, nullable=True, default=0, comment='预约不能超过1本')
    user_credit = db.Column(db.Integer, nullable=True, default=0, comment='信用机制 暂时没用')
    user_create_time = db.Column(db.DateTime, nullable=True, comment='用户创建时间')
    user_last_login_time = db.Column(db.DateTime, nullable=True, comment='用户上次登陆时间')

    def __init__(self, user_name, user_password, user_role, create_time):
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_create_time = create_time

    def keys(self):
        return ['user_name', 'user_role', 'user_borrowing', 'user_reserving', 'user_credit', 'user_last_login_time']

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return '<User user_name: {}>'.format(self.user_name)
