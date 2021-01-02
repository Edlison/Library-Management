from flask import  jsonify
from backend.api.interview.mapper.interview_SQL import insert,search
import request

from backend.api.interview import interview_blu
from backend.result.system_result import SystemResult


@interview_blu.route('/addinterviews/',methods = ['POST'])
def addinterviews():
    #获取信息
    book_ISBN = request.get_data('book_ISBN')
    book_name = request.get_data('book_name')
    book_price = request.get_data('book_price')
    book_author = request.get_data('book_author')
    book_public_company = request.get_data('book_public_company')
    book_num = request.get_data('book_num')
    user_id = request.get_data('user_id')
    #插入
    try:
        insert(book_ISBN, book_name, book_price, book_author, book_public_company, book_num, user_id)
        res = SystemResult().ok()
        return jsonify(dict(res))
    except (ImportError):
        res = SystemResult().error()
        return jsonify(dict(res))


@interview_blu.route('/showinterviews/',methods = ['POST'])
def showinterviews():
    #获得数组
    interview_search = search()
    #规范化返回
    res = SystemResult().ok()
    res.set_data(interview_search)
    return jsonify(dict(res))