from flask import  jsonify,request

from backend.api import db
from backend.api.interview.mapper.interview_SQL import insert,search


from backend.api.interview import interview_blu
from backend.result.system_result import SystemResult


@interview_blu.route('/addinterviews/',methods = ['POST'])
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


@interview_blu.route('/showinterviews/',methods = ['GET'])
def showinterviews():
    #获得数组
    interview_search = search()
    #规范化返回
    res = SystemResult().ok()
    res.set_data(interview_search)
    return jsonify(dict(res))

@interview_blu.route('/create/',methods = ['GET'])
def create():
    try:
        db.create_all()
        return "chenggong"
    except :
        return "shibai"