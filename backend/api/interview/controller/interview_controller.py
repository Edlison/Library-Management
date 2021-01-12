from flask import  jsonify,request
from backend.api import db
from backend.api.interview.mapper.interview_SQL import insert, search, drop_interview_one, search_book_ISBN
from backend.api.interview import interview_blu
from backend.result.system_result import SystemResult
from backend.filter.login_filter import need_login


@interview_blu.route('/addinterviews',methods = ['POST'])
@need_login
def addinterviews():
    #获取信息
    book_ISBN = request.form['book_ISBN']
    book_name = request.form['book_name']
    book_price = request.form['book_price']
    book_author = request.form['book_author']
    book_public_company = request.form['book_public_company']
    book_num = request.form['book_num']
    user_id = request.form['user_id']
    #插入
    try:
        insert(book_ISBN, book_name, book_price, book_author, book_public_company, book_num, user_id)
        res = SystemResult().ok()
        return jsonify(dict(res))
    except (ImportError):
        res = SystemResult().error()
        return jsonify(dict(res))


@interview_blu.route('/showinterviews',methods = ['GET'])
@need_login
def showinterviews():
    #获得数组
    interview_search = search()
    #规范化返回
    res = SystemResult().ok()
    res.set_data(interview_search)
    return jsonify(dict(res))


@interview_blu.route('/drop_interview/', methods=['POST'])
@need_login
def drop_interview():
    book_ISBN = request.form['book_ISBN']
    book = search_book_ISBN(book_ISBN)
    for each in book:
        drop_interview_one(each)
    res = SystemResult().ok()
    res.set_data("删除成功")
    return jsonify(dict(res))



@interview_blu.route('/create',methods = ['GET'])
@need_login
def create():
    db.create_all()
    return 'ok'
