import json
import request
from flask import jsonify
from backend.api.catalog.mapper.catalog_SQL import insert_noreturn,insert_return
from backend.api.catalog.mapper.catalog_SQL import search_book_ISBN,search_catalog_id,search_all,search_state,search_book_state
from backend.api.catalog.mapper.catalog_SQL import update_book_num
from backend.api.catalog import catalog_blu
from backend.result.system_result import SystemResult


@catalog_blu.route('/addcatalog_one/',methods = ['POST'])
def addcatalog_one():
    catalog_id = request.get_data('catalog_id')
    book_ISBN = request.get_data('book_ISBN')
    book_name = request.get_data('book_name')
    book_author = request.get_data('book_author')
    book_public_company = request.get_data('book_public_company')
    book_num = request.get_data('book_num')
    book_state = request.get_data('book_state')
    # if catalog_id == "":
    #     res = SystemResult().error()
    #     res.set_data("编目编号为空")
    #     return jsonify(dict(res))
    # elif book_ISBN == "":
    #     res = SystemResult().error()
    #     res.set_data("ISBN号为空")
    #     return jsonify(dict(res))
    # elif book_name == "":
    #     res = SystemResult().error()
    #     res.set_data("书名为空")
    #     return jsonify(dict(res))
    # elif book_author == "":
    #     res = SystemResult().error()
    #     res.set_data("作者为空")
    #     return jsonify(dict(res))
    # elif book_public_company == "":
    #     res = SystemResult().error()
    #     res.set_data("出版社为空")
    #     return jsonify(dict(res))
    # elif book_num <= 0:
    #     res = SystemResult().error()
    #     res.set_data("图书数量不得小于0")
    #     return jsonify(dict(res))
    # elif book_state not in [0,1]:
    #     res = SystemResult().error()
    #     res.set_data("图书状态错误")
    #     return jsonify(dict(res))
    if search_book_ISBN(book_ISBN) != ():
        res = SystemResult().error()
        res.set_data("书目已有编号")
        return jsonify(dict(res))
    elif search_catalog_id(catalog_id) != ():
        res = SystemResult().error()
        res.set_data("编目号已有")
        return jsonify(dict(res))
    else:
        if book_state == 1:
            insert_noreturn(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num)
        if book_state == 0:
            book_return_reason = request.get_data('book_return_reason')
            insert_return(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num,book_return_reason)
        res = SystemResult().ok()
        res.set_data("编目成功")
        return jsonify(dict(res))

@catalog_blu.route('/addcatalog_list/',methods = ['POST'])
def addcatalog_list():
    #获取json数组
    json_list = request.get_json()
    count = 0
    #对数组中的每一个json进行处理
    for each in json_list:
        #转换成字典
        catalog = json.loads(each)
        book_ISBN = catalog.get('book_ISBN')#ISBN
        book_name = catalog.get('book_name')#书名
        book_author = catalog.get('book_author')#作者
        book_public_company = catalog.get('book_public_company')#出版社
        book_num = catalog.get('book_num')#数量
        book_state = catalog.get('book_state')#状态
        book_return_reason = catalog.get('book_return_reason')#退货原因
        #求当前编目
        if search_catalog_id(count) == ():
            catalog_id = count
        else :
            count = count + 1
        #是否已经存在编目
        if search_book_ISBN(book_ISBN) == ():
            #不存在编目
            #根据状态判断是否有退货原因
            if book_state == 1 :
                insert_noreturn(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num)
            if book_state == 0 :
                insert_return(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num,
                              book_return_reason)
            count = count + 1
        else:
            #判断是否都有了
            if search_book_state(book_ISBN) == [0,1]:
                update_book_num(book_state,book_num)
                continue
            elif search_book_state(book_ISBN) == book_state:
                continue
            else:
                if book_state == 1:
                    insert_noreturn(catalog_id, book_ISBN, book_name, book_author, book_public_company, book_state,
                                    book_num)
                if book_state == 0:
                    insert_return(catalog_id, book_ISBN, book_name, book_author, book_public_company, book_state,
                                  book_num, book_return_reason)
                count = count + 1
    res = SystemResult().ok()
    res.set_data("编目成功")
    return jsonify(dict(res))

@catalog_blu.route('/catalog_search_ISBN/',methods = ['POST'])
def catalog_searh():
    book_ISBN = request.get_data('ISBN')
    # 获得数组
    catalog_list = search_book_ISBN(book_ISBN)
    # 用来存储转换成json格式的列表
    catalog_jsonlist = []
    # 转换格式并存储
    for each in catalog_list:
        catalog_jsonlist.append(dict(each))
    # 转换成json数组
    catalog_json = json.dumps(catalog_jsonlist, ensure_ascii=False)
    # 规范化返回
    res = SystemResult().ok()
    res.set_data(catalog_json)
    return jsonify(dict(res))

@catalog_blu.route('/showcatalog/',methods = ['POST'])
def showcatalog():
    #获得数组
    catalog_search = search_all()
    #规范化返回
    res = SystemResult().ok()
    res.set_data(catalog_search)
    return jsonify(dict(res))

@catalog_blu.route('/show_return_catalog/',methods = ['POST'])
def show_return_catalog():
    #获得数组
    catalog_search = search_state()
    #规范化返回
    res = SystemResult().ok()
    res.set_data(catalog_search)
    return jsonify(dict(res))