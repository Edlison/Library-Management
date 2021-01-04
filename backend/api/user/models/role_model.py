# @Author  : Edlison
# @Date    : 12/31/20 18:11
from backend.api import db


class Role(db.Model):
    __tablename__ = 'role'
    role_id = db.Column(db.Integer, primary_key=True)
    role_rights = db.Column(db.String(10))

