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


def get_borrowing_books_by_user_name(user_name):
    """
    通过用户名获取所有借阅信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 12:13
    """
    borrowings = Borrowing.query.filter(Borrowing.borrow_user_name == user_name).all()
    return borrowings


def get_borrowing_books_all():
    borrowngs = Borrowing.query.all()
    return borrowngs


def get_reservation_books_all():
    reservations = Reservation.query.all()
    return reservations


def get_resr_book_by_user_name(user_name):
    """
    通过用户名获取预约信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 14:34
    """
    reservation = Reservation.query.filter(Reservation.reser_user_name == user_name).first()
    return reservation


def get_all_books_in_catalog():
    """
    获取所有图书

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:56
    """
    books = Catalog.query.all()
    return books


def get_borrowing_by_id(borrow_id):
    """
    通过id获取借阅图书信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:56
    """
    borrowing = Borrowing.query.filter_by(borrow_id=borrow_id).first()
    return borrowing


def renew_borrowing_by_id(borrow_id):
    """
    通过id续借图书 默认续借1个月

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:57
    """
    borrowing = Borrowing.query.filter_by(borrow_id=borrow_id).first()
    # 续借机会减1
    borrowing.borrow_renew_left -= 1
    # 续借时间加1月
    end_time = borrowing.borrow_end_time
    end_time = add_months(end_time, 1)
    borrowing.borrow_end_time = end_time
    db.session.commit()


def delete_borrowing_by_id(borrow_id):
    """
    通过id删除借阅信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:57
    """
    borrowing = Borrowing.query.filter_by(borrow_id=borrow_id).first()
    db.session.delete(borrowing)
    db.session.commit()


def increase_remainder(book_ISBN):
    """
    增加库存

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 11:19
    """
    catalog = Catalog.query.filter(Catalog.book_ISBN == book_ISBN).first()
    catalog.book_remainder_num += 1
    db.session.commit()


def get_resr_by_id(reser_id):
    """
    通过id获取预约信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:58
    """
    reservation = Reservation.query.filter_by(reser_id=reser_id).first()
    return reservation


def delete_resr_by_id(reser_id):
    """
    通过id删除预约信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:58
    """
    reservation = Reservation.query.filter_by(reser_id=reser_id).first()
    db.session.delete(reservation)
    db.session.commit()
