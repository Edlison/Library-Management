# @Author  : Edlison
# @Date    : 12/31/20 17:37
from backend.api import db


class Borrowing(db.Model):
    __tablename__ = 'borrowing'
    borrow_user_id = db.Column(db.Integer, primary_key=True)
    borrow_book_id = db.Column(db.Integer, primary_key=True)
    borrow_renew_left = db.Column(db.Integer, default=1)
    borrow_start_time = db.Column(db.DateTime)
    borrow_end_time = db.Column(db.DateTime)

