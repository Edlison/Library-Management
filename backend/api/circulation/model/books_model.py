# @Author  : Edlison
# @Date    : 12/31/20 17:46
from backend.api import db


class Books(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(255))
    book_num = db.Column(db.Integer)
