from backend.api import db


class Catalog(db.Model):
    __tablename__ = 'catalog'
    catalog_id = db.Column(db.Integer, primary_key=True)
    book_ISBN = db.Column(db.String(17), nullable=True)
    book_name = db.Column(db.String(50), nullable = True)
    book_author = db.Column(db.String(50),nullable = True)
    book_public_company = db.Column(db.String(50),nullable = True)
    book_num = db.Column(db.Integer,nullable = True, default = 1)
    book_state = db.Column(db.Integer,nullable = True)
    book_catalog_time = db.Column(db.DateTime,nullable = True, default = 'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    book_return_reason = db.Column(db.String(50))

    def keys(self):
        return ['catalog_id',
                'book_ISBN',
                'book_name',
                'book_author',
                'book_public_company',
                'book_num',
                'book_state',
                'book_catalog_time',
                'book_return_reason']

    def __getitem__(self, item):
        return getattr(self, item)
