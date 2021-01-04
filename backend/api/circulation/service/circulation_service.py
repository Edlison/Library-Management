# @Author  : Edlison
# @Date    : 1/3/21 16:46
from backend.result.system_result import SystemResult
from backend.api.user.mapper.user_mapper import get_user_by_name, update_user_borrowing
from backend.api.circulation.mapper.circulation_mapper import get_book_by_isbn, add_borrow


def borrow_book(user_name, book_ISBN):
    user = get_user_by_name(user_name)
    book = get_book_by_isbn(book_ISBN)
    res = SystemResult()
    if user:
        if user.user_borrowing and user.user_borrowing < 3:  # 用户借阅数小于3
            if book.book_left and book.book_left > 1:  # 图书库存大于1 TODO catalog表中余量
                add_borrow(user_name, book_ISBN)
                update_user_borrowing(user_name)
                res = SystemResult().ok('借阅成功')
            else:
                res = SystemResult().error('图书已无余量')
        else:
            res = SystemResult().error('借阅已经到达上限 不能借阅')
    else:
        res = SystemResult().error('用户错误')

    return res
