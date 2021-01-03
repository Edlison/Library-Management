from datetime import datetime

from backend.api import db


class Interview(db.Model):
    __tablename__ = 'interview'
    interview_id = db.Column(db.Integer, primary_key=True)
    book_ISBN = db.Column(db.String(17), nullable=True)
    book_name = db.Column(db.String(50), nullable = True)
    book_price = db.Column(db.Integer)
    book_author = db.Column(db.String(50),nullable = True)
    book_public_company = db.Column(db.String(50),nullable = True)
    book_num = db.Column(db.Integer,nullable = True, default = 1)
    book_interview_time = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))

    def keys(self):
        return ['interview_id',
                'book_ISBN',
                'book_name',
                'book_price',
                'book_author',
                'book_public_company',
                'book_num',
                'book_interview_time',
                'user_id']

    def __getitem__(self, item):
        return getattr(self, item)

