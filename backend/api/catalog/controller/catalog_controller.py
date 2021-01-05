import json
from flask import jsonify, request
from backend.api.catalog.mapper.catalog_SQL import search_book_ISBN, search_catalog, \
    update_catalog_book_num_add, update_catalog_book_num_sub, \
    insert_noreturn, drop_catalog_id
from backend.api.catalog.mapper.return_SQL import search_return_book, search_return_book_ISBN, \
    update_return_book_book_num, insert_return
from backend.api.catalog.service.catalog_sercive import create_catalog_id
from backend.api.catalog import catalog_blu
from backend.result.system_result import SystemResult
from backend.filter.login_filter import need_login


@catalog_blu.route('/addcatalog_one',methods = ['POST'])
@need_login
def addcatalog_one():
    # 获取数据
    book_ISBN = request.form['book_ISBN']
    book_name = request.form['book_name']
    book_author = request.form['book_author']
    book_public_company = request.form['book_public_company']
    book_num = request.form['book_num']
    book_state = request.form['book_state']
    book_class = request.form['book_class']
    # 判断书是否已经有编目
    if book_state == '1':
        # 存入” catalog “
        if not search_book_ISBN(book_ISBN):
            # 存新的编目
            catalog_id = create_catalog_id(book_class)
            insert_noreturn(catalog_id, book_ISBN, book_name, book_author, book_public_company, book_num)
            res = SystemResult().ok()
            res.set_data(["编目成功", catalog_id])
            return jsonify(dict(res))
        else:
            # 已有编目，更新数量
            update_catalog_book_num_add(book_ISBN, book_num)
            res = SystemResult().ok()
            res.set_data(["书目已有编目", "更新编目数量成功"])
            return jsonify(dict(res))
    elif book_state == '0':
        if search_return_book_ISBN(book_ISBN) == []:
            book_return_reason = request.form['book_return_reason']
            book_seller = request.form['book_seller']
            insert_return(book_ISBN, book_name, book_author, book_public_company, book_num, book_return_reason, book_seller)
            res = SystemResult().ok()
            res.set_data(["编目成功", "退货"])
            return jsonify(dict(res))
        else:
            update_return_book_book_num(book_ISBN, book_num)
            res = SystemResult().ok()
            res.set_data(["书目已有编目", "更新退货数量成功"])
            return jsonify(dict(res))


@catalog_blu.route('/addcatalog_list',methods = ['POST'])
@need_login
def addcatalog_list():
    # 获取json数组
    json_list = json.loads(request.get_data(as_text=True))
    catalog_id_list = []
    # 对数组中的每一个json进行处理
    for each in json_list:
        # 转换成字典
        book_ISBN = each.get("book_ISBN")  # ISBN
        book_name = each.get("book_name")  # 书名
        book_author = each.get("book_author")  # 作者
        book_public_company = each.get("book_public_company")  # 出版社
        book_class = each.get("book_class")
        book_num = each.get("book_num")  # 数量
        book_state = each.get("book_state")  # 状态
        # 判断书是否已经有编目
        if book_state == 1:
            # 存入” catalog “
            if search_book_ISBN(book_ISBN) == []:
                # 存新的编目
                catalog_id = create_catalog_id(book_class)
                catalog_id_list.append({"name": book_name, "catalog": catalog_id})
                insert_noreturn(catalog_id, book_ISBN, book_name, book_author, book_public_company, book_num)
            else:
                # 已有编目，更新数量
                update_catalog_book_num_add(book_ISBN, book_num)
        elif book_state == 0:
            if search_return_book_ISBN(book_ISBN) == []:
                book_return_reason = each.get("book_return_reason")
                book_seller = each.get("book_seller")
                insert_return(book_ISBN, book_name, book_author, book_public_company, book_num, book_return_reason,
                              book_seller)
            else:
                update_return_book_book_num(book_ISBN, book_num)
    if catalog_id_list == []:
        res = SystemResult().error()
        res.set_data(["所有图书已被重复编目"])
        return jsonify(dict(res))
    else:
        res = SystemResult().ok()
        res.set_data(catalog_id_list)
        return jsonify(dict(res))
    # 返回ISBN和编目号


@catalog_blu.route('/catalog_search_ISBN',methods = ['POST'])
@need_login
def catalog_searh():
    book_ISBN = request.form['book_ISBN']
    # 获得数组
    catalog_list = search_book_ISBN(book_ISBN)
    # 用来存储转换成json格式的列表
    catalog_jsonlist = []
    # 转换格式并存储
    for each in catalog_list:
        catalog_jsonlist.append(dict(each))
    # 转换成json数组
    catalog_json = json.dumps(catalog_jsonlist, default=str, ensure_ascii=False)
    catalog_json = json.loads(catalog_json)
    # 规范化返回
    res = SystemResult().ok()
    res.set_data(catalog_json)
    return jsonify(dict(res))


@catalog_blu.route('/showcatalog',methods = ['GET'])
@need_login
def showcatalog():
    # 获得数组
    catalog_search = search_catalog()
    # 规范化返回
    res = SystemResult().ok()
    res.set_data(catalog_search)
    return jsonify(dict(res))


@catalog_blu.route('/show_return_catalog',methods = ['GET'])
@need_login
def show_return_catalog():
    # 获得数组
    returnbook_search = search_return_book()
    # 规范化返回
    res = SystemResult().ok()
    res.set_data(returnbook_search)
    return jsonify(dict(res))


@catalog_blu.route('/drop_catalog/', methods=['POST'])
def drop_catalog():
    book_ISBN = request.form['book_ISBN']
    book = search_book_ISBN(book_ISBN)[0]
    if book.book_num == book.book_remainder_num:
        drop_catalog_id(book)
        res = SystemResult().ok()
        res.set_data(["删除成功"])
        return jsonify(dict(res))
    else:
        res = SystemResult().error()
        res.set_data(["删除失败", "有图书被借出"])
        return jsonify(dict(res))
    # 删除所有的书


@catalog_blu.route('/report_loss/', methods=['POST'])
def report_loss():
    book_ISBN = request.form['book_ISBN']
    book_num = request.form['book_num']
    book = search_book_ISBN(book_ISBN)[0]
    if (book.book_remainder_num - int(book_num)) > 1:
        update_catalog_book_num_sub(book_ISBN, book_num)
        res = SystemResult().ok()
        res.set_data(["报损成功"])
        return jsonify(dict(res))
    else:
        res = SystemResult().error()
        res.set_data(["报损失败", "图书在馆数量不足"])
        return jsonify(dict(res))
    # 报损图书，减少数量
