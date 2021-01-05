# @Author  : Edlison
# @Date    : 1/3/21 16:46
from backend.result.system_result import SystemResult
from backend.api.user.mapper.user_mapper import get_user_by_name, add_user_borrowing, add_user_reser, reduce_user_borrowing, reduce_user_reser
from backend.api.circulation.mapper.circulation_mapper import \
    get_book_by_isbn, add_borrow, add_reser, reduce_remainder, get_borrowing_books_by_user_name, get_resr_book_by_user_name, \
    get_all_books_in_catalog, get_borrowing_by_id, renew_borrowing_by_id, delete_borrowing_by_id, increase_remainder, \
    get_resr_by_id, delete_resr_by_id, get_borrowing_books_all, get_reservation_books_all
from backend.util.serialize import serialize_model_list, serialize_model
from backend.util.datetime_cmp import is_dt_later
import datetime


def borrow_book(user_name, book_ISBN):
    """
    借书流程
    
    Args:
    
    Returns:
    
    @Author  : Edlison
    @Date    : 1/4/21 16:53
    """
    user = get_user_by_name(user_name)
    book = get_book_by_isbn(book_ISBN)
    res = SystemResult()
    if user:
        if user.user_borrowing is not None and user.user_borrowing < 3:  # 用户借阅数小于3
            if book is not None and book.book_remainder_num is not None and book.book_remainder_num > 1:  # 图书库存大于1
                reduce_remainder(book_ISBN)
                add_borrow(user_name, book_ISBN)
                add_user_borrowing(user_name)
                res.ok('借阅成功')
            else:
                res.error('图书已无余量')
        else:
            res.error('借阅已经到达上限 不能借阅')
    else:
        res.error('用户错误')
    return res


def reser_book(user_name, book_ISBN):
    """
    预约流程

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:54
    """
    user = get_user_by_name(user_name)
    book = get_book_by_isbn(book_ISBN)
    res = SystemResult()
    if user:
        if user.user_reserving is not None and user.user_reserving < 1:
            if book is not None and book.book_remainder_num is not None and book.book_remainder_num > 1:
                reduce_remainder(book_ISBN)
                add_reser(user_name, book_ISBN)
                add_user_reser(user_name)
                res.ok('预约成功')
            else:
                res.error('图书已无余量')
        else:
            res.error('预约已达上限 不能预约')
    else:
        res.error('用户错误')
    return res


def get_borrow_books(user_name):
    """
    获取用户的在借书籍信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:54
    """
    books = get_borrowing_books_by_user_name(user_name)
    res = SystemResult()
    books = serialize_model_list(books)
    if len(books) > 0:
        for book in books:
            book_detail = get_book_by_isbn(book['borrow_book_isbn'])
            book['borrow_book_name'] = book_detail.book_name
        res.set_data(books)
        res.ok('获取借阅信息成功')
    else:
        res.ok('没有借阅信息')
    print(books)
    print(res)
    return res


def get_borrow_all():
    """
    获取全部借阅信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/5/21 16:51
    """
    books = get_borrowing_books_all()
    res = SystemResult()
    if books:
        books = serialize_model_list(books)
        for book in books:
            book_detail = get_book_by_isbn(book['borrow_book_isbn'])
            book['borrow_book_name'] = book_detail['book_name']
        res.set_data(books)
        res.ok('获取全部借阅图书成功')
    else:
        res.error('获取借阅图书失败')
    return res


def get_resr_book(user_name):
    """
    获取用户的在预约书籍信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:54
    """
    book = get_resr_book_by_user_name(user_name)
    res = SystemResult()
    if book:
        book_detail = get_book_by_isbn(book.reser_book_isbn)
        if book_detail:
            res.set_data(serialize_model(book))
            res.data['reser_book_name'] = book_detail.book_name
            res.ok('获取预约信息成功')
        else:
            res.error('获取图书详细信息失败')
    else:
        res.ok('没有预约信息')
    return res


def get_resr_all():
    """
    获取全部预约信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/5/21 16:51
    """
    books = get_reservation_books_all()
    res = SystemResult()
    if books:
        books = serialize_model_list(books)
        for book in books:
            book_detail = get_book_by_isbn(book['borrow_book_isbn'])
            book['borrow_book_name'] = book_detail['book_name']
        res.set_data(books)
        res.ok('获取全部预约图书成功')
    else:
        res.error('获取预约图书失败')
    return res


def get_certain_book(book_ISBN):
    """
    获取某本书的详细信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:55
    """
    book = get_book_by_isbn(book_ISBN)
    res = SystemResult()
    if book:
        res.set_data(serialize_model(book))
        res.ok('获取图书信息成功')
    else:
        res.error('获取图书信息失败')
    return res


def get_all_books():
    """
    获取全部馆藏书籍信息

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:55
    """
    books = get_all_books_in_catalog()
    res = SystemResult()
    if books:
        res.set_data(serialize_model_list(books))
        res.ok('获取馆藏信息成功')
    else:
        res.error('获取馆藏信息失败')
    return res


def renew_book(borrow_id):
    """
    续借图书 默认1个月

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:55
    """
    book = get_borrowing_by_id(borrow_id)
    res = SystemResult()
    if book:
        if book.borrow_renew_left > 0:
            renew_borrowing_by_id(borrow_id)
            res.ok('续借成功')
        else:
            res.error('不可再次续借')
    else:
        res.error('未找到该图书')
    return res


def return_book(user_name, borrow_id):
    """
    还书

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:55
    """
    book = get_borrowing_by_id(borrow_id)
    res = SystemResult()
    if book:
        delete_borrowing_by_id(book.borrow_id)
        increase_remainder(book.borrow_book_isbn)
        reduce_user_borrowing(user_name)
        res.ok('还书成功')
    else:
        res.error('没有找到在借的这本书')
    return res


def cancel_resr(user_name, reser_id):
    """
    取消预约

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:55
    """
    book = get_resr_by_id(reser_id)
    res = SystemResult()
    if book:
        delete_resr_by_id(book.reser_id)
        increase_remainder(book.reser_book_isbn)
        reduce_user_reser(user_name)
        res.ok('取消预约成功')
    else:
        res.error('没有找到在预约的这本书')
    return res


def resr_to_borrow(user_name, reser_id):
    """
    预约图书转为在借图书

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:56
    """
    user = get_user_by_name(user_name)
    res = SystemResult()
    if user:
        if user.user_borrowing is not None and user.user_borrowing < 3:
            book = get_resr_by_id(reser_id)
            now = datetime.datetime.now()
            if is_dt_later(now, book.reser_start_time) and is_dt_later(book.reser_end_time, now):
                delete_resr_by_id(book.reser_id)
                reduce_user_reser(user.user_name)
                add_borrow(user.user_name, book.reser_book_isbn)
                add_user_borrowing(user.user_name)
                res.ok('预约转借阅成功')
            else:
                cancel_resr(user_name, reser_id)
                res.error('不再预约时间内 无法借阅 已自动取消预约')
        else:
            res.error('借阅已经到达上限 不能借阅')
    else:
        res.error('获取用户失败')
    return res
