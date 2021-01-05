import json
from backend.api import db
from backend.api.catalog.models.return_model import Return


def insert_return(book_ISBN, book_name, book_author, book_public_company, book_num, book_return_reason, book_seller):
    # 创建对象
    return_book = Return(
        book_ISBN=book_ISBN,
        book_name=book_name,
        book_author=book_author,
        book_public_company=book_public_company,
        book_num=book_num,
        book_return_reason=book_return_reason,
        book_seller=book_seller)
    # 插入新数据
    db.session.add(return_book)
    # 提交数据到数据库
    db.session.commit()


def search_return_book_ISBN(book_ISBN):
    return_book_list = Return.query.filter(Return.book_ISBN == book_ISBN).all()
    return return_book_list


def search_return_book():
    # 获得退货清单内所有的内容
    return_book_list = Return.query.filter().all()
    # 用来存储转换成json格式的列表
    return_book_jsonlist = []
    # 转换格式并存储
    for each in return_book_list:
        return_book_jsonlist.append(dict(each))
    # 转换成json数组
    return_book_json = json.dumps(return_book_jsonlist, default=str, ensure_ascii=False)
    return_book_json = json.loads(return_book_json)
    # 返回数组
    return return_book_json


def update_return_book_book_num(book_ISBN,book_return_reason, book_num):
    # 更新书的数量，通过ISBN以及书的状态查询书的实体
    return_book = Return.query.filter(Return.book_ISBN == book_ISBN,Return.book_return_reason == book_return_reason).first()
    # 更新数量
    return_book.book_num = return_book.book_num + int(book_num)
    # 提交数据
    db.session.commit()
