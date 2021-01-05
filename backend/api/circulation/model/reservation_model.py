# @Author  : Edlison
# @Date    : 12/31/20 12:35
from backend.api import db


class Reservation(db.Model):
    __tablename__ = 'reservation'
    reser_id = db.Column(db.Integer, primary_key=True, comment='预约主键')
    reser_user_name = db.Column(db.String(32), comment='用户名')
    reser_book_isbn = db.Column(db.String(17), comment='图书ISBN号')
    reser_start_time = db.Column(db.DateTime, comment='预约开始时间')
    reser_end_time = db.Column(db.DateTime, comment='预约结束时间')

    def __init__(self, user_name, book_isbn, start_time, end_time):
        self.reser_user_name = user_name
        self.reser_book_isbn = book_isbn
        self.reser_start_time = start_time
        self.reser_end_time = end_time

    def keys(self):
        return ['reser_id', 'reser_user_name', 'reser_book_isbn', 'reser_start_time', 'reser_end_time']

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return '<Reservation reser_id: {}>'.format(self.reser_id)
