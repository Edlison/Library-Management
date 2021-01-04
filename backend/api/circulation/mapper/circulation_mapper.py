# @Author  : Edlison
# @Date    : 1/4/21 00:46
from backend.api import db
from backend.api.catalog.models.catalog_model import Catalog
from backend.api.circulation.model.borrowing_model import Borrowing
from backend.api.circulation.model.reservation_model import Reservation
import datetime
from backend.util.dt_util import add_months


def get_book_by_isbn(book_ISBN):
    """
    通过ISBN获取图书

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 01:19
    """
    catalog = Catalog.query.filter(Catalog.book_ISBN==book_ISBN).first()
    return catalog


def add_borrow(user_name, book_ISBN):
    """
    添加借阅信息

    Args:

    Returns: n

    @Author  : Edlison
    @Date    : 1/4/21 01:28
    """
    start_time = datetime.datetime.now()
    end_time = add_months(start_time, 3)
    borrowing = Borrowing(user_name, book_ISBN, start_time, end_time)
    n = db.session.add(borrowing)
    db.session.commit()
    return n


def add_reser(user_name, book_ISBN):
    """
    增加预约信息

    Args:

    Returns: n

    @Author  : Edlison
    @Date    : 1/4/21 11:40
    """
    start_time = datetime.datetime.now()
    end_time = add_months(start_time, 3)
    reservation = Reservation(user_name, book_ISBN, start_time, end_time)
    n = db.session.add(reservation)
    db.session.commit()
    return n


def reduce_remainder(book_ISBN):
    """
    减少库存

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 11:19
    """
    catalog = Catalog.query.filter(Catalog.book_ISBN == book_ISBN).first()
    catalog.book_remainder_num -= 1
    db.session.commit()

