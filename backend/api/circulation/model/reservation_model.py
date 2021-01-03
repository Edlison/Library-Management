# @Author  : Edlison
# @Date    : 12/31/20 12:35
from backend.api import db


class Reservation(db.Model):
    __tablename__ = 'reservation'
    reser_user_id = db.Column(db.Integer, primary_key=True)
    reser_book_id = db.Column(db.Integer, primary_key=True)
    reser_start_time = db.Column(db.DateTime)
    reser_end_time = db.Column(db.DateTime)


