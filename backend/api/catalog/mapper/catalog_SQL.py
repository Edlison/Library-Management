import json
from backend.api import db
from backend.api.catalog.models.catalog_model import Catalog


def insert_return(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num,book_return_reason):
    catalog = Catalog(catalog_id=catalog_id,
                      book_ISBN=book_ISBN,
                      book_name=book_name,
                      book_author=book_author,
                      book_public_company=book_public_company,
                      book_state=book_state,
                      book_num=book_num,
                      book_remainder_num=book_num,
                      book_return_reason=book_return_reason)
    db.session.add(catalog)
    db.session.commit()

def insert_noreturn(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_state,book_num):
    catalog = Catalog(catalog_id=catalog_id,
                      book_ISBN=book_ISBN,
                      book_name=book_name,
                      book_author=book_author,
                      book_public_company=book_public_company,
                      book_state=book_state,
                      book_num=book_num,
                      book_remainder_num=book_num)
    db.session.add(catalog)
    db.session.commit()

def search_book_ISBN(book_ISBN):
    catalog_list = Catalog.query.filter(Catalog.book_ISBN == book_ISBN).all()
    return catalog_list

def search_catalog_id(catalog_id):
    catalog_list = Catalog.query.filter(Catalog.catalog_id == catalog_id).all()
    return catalog_list

def search_book_state(book_ISBN):
    catalog_list = Catalog.query.filter(Catalog.book_ISBN == book_ISBN)
    state_list = []
    for each in catalog_list:
        state_list.append(each.book_state)
    return state_list

def search_all():
    #获得采访清单内所有的内容
    catalog_list =  Catalog.query.all()
    #用来存储转换成json格式的列表
    catalog_jsonlist = []
    #转换格式并存储
    for each in catalog_list:
        catalog_jsonlist.append(dict(each))
    #转换成json数组
    catalog_json = json.dumps(catalog_jsonlist,default=str,ensure_ascii=False)
    catalog_json = json.loads(catalog_json)
    #返回数组
    return catalog_json

def search_state():
    # 获得采访清单内所有的内容
    catalog_list = Catalog.query.filter(Catalog.book_state == 0).all()
    # 用来存储转换成json格式的列表
    catalog_jsonlist = []
    # 转换格式并存储
    for each in catalog_list:
        catalog_jsonlist.append(dict(each))
    # 转换成json数组
    catalog_json = json.dumps(catalog_jsonlist, default=str, ensure_ascii=False)
    catalog_json = json.loads(catalog_json)
    # 返回数组
    return catalog_json

def update_book_num(book_state,book_num):
    catalog = Catalog.query.filter(Catalog.book_state == book_state)
    catalog.book_num = catalog.book_num+book_num
    catalog.book_remainder_num = catalog.book_remainder_num + book_num
    db.session.commit()
