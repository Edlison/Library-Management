import json
from flask import jsonify,request
from backend.api.catalog.mapper.catalog_SQL import insert_noreturn,insert_return
from backend.api.catalog.mapper.catalog_SQL import search_book_ISBN,search_all,search_state,search_catalog_id,search_book_state
from backend.api.catalog.mapper.catalog_SQL import update_book_num
from backend.api.catalog.service.catalog_sercive import create_catalog_id
from backend.api.catalog import catalog_blu
from backend.result.system_result import SystemResult


@catalog_blu.route('/addcatalog_one/',methods = ['POST'])
def addcatalog_one():
    book_ISBN = request.form['book_ISBN']
    book_name = request.form['book_name']
    book_author = request.form['book_author']
    book_public_company = request.form['book_public_company']
    book_num = request.form['book_num']
    book_state = request.form['book_state']
    book_class = request.form['book_class']
    # print(book_ISBN,book_name,book_author,book_public_company,book_state,book_num,book_state)
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
    if search_book_ISBN(book_ISBN) != []:
        print(search_book_ISBN(book_ISBN))
        res = SystemResult().error()
        res.set_data("书目已有编号")
        return jsonify(dict(res))
    else:
        catalog_id = create_catalog_id(book_class)
        if book_state == '1':
            insert_noreturn(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num)
            res = SystemResult().ok()
            res.set_data(["编目成功", "退货"])
            return jsonify(dict(res))
        if book_state == '0':
            book_return_reason = request.get_data('book_return_reason')
            insert_return(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num,book_return_reason)
            res = SystemResult().ok()
            res.set_data(["编目成功", catalog_id])
            return jsonify(dict(res))
        #返回编目成功以及编目号
        #退货的就不传编目号

@catalog_blu.route('/addcatalog_list/',methods = ['POST'])
def addcatalog_list():
    #获取json数组
    json_list = json.loads(request.get_data(as_text=True))
    catalog_id_list = []
    #对数组中的每一个json进行处理
    for each in json_list:
        #转换成字典
        book_ISBN = each.get("book_ISBN")#ISBN
        book_name = each.get("book_name")#书名
        book_author = each.get("book_author")#作者
        book_public_company = each.get("book_public_company")#出版社
        book_class = each.get("book_class")
        book_num = each.get("book_num")#数量
        book_state = each.get("book_state")#状态
        book_return_reason = each.get("book_return_reason")#退货原因
        #是否已经存在编目
        if search_book_ISBN(book_ISBN) == []:
            #不存在编目
            # #求当前编目
            catalog_id = create_catalog_id(book_class)
            #根据状态判断是否有退货原因
            if book_state == 1 :
                catalog_id_list.append({"name":book_name,"catalog":catalog_id})
                insert_noreturn(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num)
            if book_state == 0 :
                insert_return(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num,
                              book_return_reason)
        else:
            #判断是否都有了
            if search_book_state(book_ISBN) == [0,1]:
                update_book_num(book_ISBN,book_state,book_num)
                continue
            #与当前状态相同
            elif search_book_state(book_ISBN)[0] == book_state:
                update_book_num(book_ISBN,book_state,book_num)
                continue
            else:
                catalog_id = search_catalog_id(book_ISBN)[0].catalog_id
                if book_state == 1:
                    insert_noreturn(catalog_id, book_ISBN, book_name, book_author, book_public_company, book_state,
                                    book_num)
                if book_state == 0:
                    insert_return(catalog_id, book_ISBN, book_name, book_author, book_public_company, book_state,
                                  book_num, book_return_reason)
    if catalog_id_list == [] :
        res = SystemResult().error()
        res.set_data("所有图书已被重复编目")
        return jsonify(dict(res))
    else:
        res = SystemResult().ok()
        res.set_data(catalog_id_list)
        return jsonify(dict(res))
    #返回ISBN和编目号

@catalog_blu.route('/catalog_search_ISBN/',methods = ['POST'])
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
    print(catalog_json)
    # 规范化返回
    res = SystemResult().ok()
    res.set_data(catalog_json)
    return jsonify(dict(res))

@catalog_blu.route('/showcatalog/',methods = ['GET'])
def showcatalog():
    #获得数组
    catalog_search = search_all()
    #规范化返回
    res = SystemResult().ok()
    res.set_data(catalog_search)
    return jsonify(dict(res))

@catalog_blu.route('/show_return_catalog/',methods = ['GET'])
def show_return_catalog():
    #获得数组
    catalog_search = search_state()
    #规范化返回
    res = SystemResult().ok()
    res.set_data(catalog_search)
    return jsonify(dict(res))


