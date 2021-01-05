from datetime import datetime
from backend.api import db


class Return(db.Model):
    #建立数据表catalog
    #包括属性编目号、书的ISBN、书名、书的作者、书的出版社、书的数量、书的剩余数量、书的状态、书的最后修改时间、退货原因
    #表名为“ return ”
    __tablename__ = 'return'
    # #编目号，通过 create_catalog_id() 来创建
    # catalog_id = db.Column(db.String(10), primary_key=True)
    #书的ISBN号，每本书一个
    book_ISBN = db.Column(db.String(17), nullable=True,primary_key = True)
    #书的名字
    book_name = db.Column(db.String(50), nullable = True)
    #书的作者
    book_author = db.Column(db.String(50),nullable = True)
    #书的出版社
    book_public_company = db.Column(db.String(50),nullable = True)
    #书的退货数量
    book_num = db.Column(db.Integer,nullable = True, default = 1)
    # #书的书库剩余量
    # book_remainder_num = db.Column(db.Integer,nullable = True)
    # #书的状态，有0/1两种，0表示需要退货，1表示正常可以入库。
    # book_state = db.Column(db.Integer,nullable = True)
    #书的最后修改时间，根据系统时间自动更新
    book_catalog_time = db.Column(db.DateTime, default=datetime.now)
    #书的退货原因，当book_state = 1 时可以为空，当book_state = 0 时不可为空
    book_return_reason = db.Column(db.String(200),nullable = True,primary_key = True)
    #书的出货商
    book_seller = db.Column(db.String(50),nullable = True)


    #为了方便的转化成字典
    def keys(self):
        return [
                'book_ISBN',
                'book_name',
                'book_author',
                'book_public_company',
                'book_num',
                'book_catalog_time',
                'book_return_reason',
                'book_seller']

    def __getitem__(self, item):
        return getattr(self, item)