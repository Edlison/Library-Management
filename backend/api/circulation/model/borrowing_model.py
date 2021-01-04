# @Author  : Edlison
# @Date    : 12/31/20 17:37
from backend.api import db


class Borrowing(db.Model):
    __tablename__ = 'borrowing'
    borrow_id = db.Column(db.Integer, primary_key=True, comment='借阅主键')
    borrow_user_name = db.Column(db.String(32), comment='用户名')
    borrow_book_isbn = db.Column(db.String(17), comment='图书ISBN号')
    borrow_renew_left = db.Column(db.Integer, default=1, comment='剩余续借次数')
    borrow_start_time = db.Column(db.DateTime, comment='借阅开始时间')
    borrow_end_time = db.Column(db.DateTime, comment='借阅应还时间')

    def __init__(self, user_name, book_isbn, borrow_start_time, borrow_end_time):
        self.borrow_user_name = user_name
        self.borrow_book_isbn = book_isbn
        self.borrow_start_time = borrow_start_time
        self.borrow_end_time = borrow_end_time
