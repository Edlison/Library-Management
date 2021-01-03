# @Author  : Edlison
# @Date    : 1/3/21 16:46
from backend.result.system_result import SystemResult
from backend.api.user.mapper.user_mapper import get_user_by_name
from backend.api.circulation.mapper.circulation_mapper import get_book_by_isbn


def borrow_book(user_name, book_ISBN):
    user = get_user_by_name(user_name)
    book = get_book_by_isbn(book_ISBN)
    res = SystemResult()
    if user:
        if user.user_borrowing and user.user_borrowing < 3:
            if ...:
                ...
        else:
            res = SystemResult().error('借阅已经到达上限，不能借阅。')
    else:
        res = SystemResult().error('用户错误')

    return res