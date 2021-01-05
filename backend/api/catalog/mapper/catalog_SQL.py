import json
from backend.api import db
from backend.api.catalog.models.catalog_model import Catalog

def insert_noreturn(catalog_id,book_ISBN,book_name,book_author,book_public_company,book_num):
    #创建实体
    catalog = Catalog(catalog_id=catalog_id,
                      book_ISBN=book_ISBN,
                      book_name=book_name,
                      book_author=book_author,
                      book_public_company=book_public_company,
                      book_num=book_num,
                      book_remainder_num=book_num)
    #插入新数据
    db.session.add(catalog)
    #提交到数据库
    db.session.commit()

def search_book_ISBN(book_ISBN):
    #查询并返回一个列表，列表包括全部对象
    catalog_list = Catalog.query.filter(Catalog.book_ISBN == book_ISBN).all()
    return catalog_list

# def search_catalog_id(book_ISBN):
#     # 查询并返回一个列表，列表包括全部对象
#     catalog_list = Catalog.query.filter(Catalog.book_ISBN == book_ISBN).all()
#     return catalog_list

def search_book_class(book_class):
    # 查询并返回一个列表，列表包括全部对象
    catalog_list = Catalog.query.filter(Catalog.catalog_id.like(book_class+'%')).all()
    return catalog_list

def search_catalog():
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

def update_catalog_book_num_add(book_ISBN,book_num):
    #更新书的数量，通过ISBN以及书的状态查询书的实体
    catalog = Catalog.query.filter(Catalog.book_ISBN == book_ISBN).first()
    #更新数量
    catalog.book_num = catalog.book_num + int(book_num)
    catalog.book_remainder_num = catalog.book_remainder_num + int(book_num)
    #提交数据
    db.session.commit()

def update_catalog_book_num_sub(book_ISBN,book_num):
    #更新书的数量，通过ISBN以及书的状态查询书的实体
    catalog = Catalog.query.filter(Catalog.book_ISBN == book_ISBN).first()
    #更新数量
    catalog.book_num = catalog.book_num - int(book_num)
    catalog.book_remainder_num = catalog.book_remainder_num - int(book_num)
    #提交数据
    db.session.commit()

def drop_catalog_id(catalog):
    db.session.delete(catalog)
    db.session.commit()

#def search_state():
#     # 获得编目内所有的内容
#     catalog_list = Catalog.query.filter().all()
#     # 用来存储转换成json格式的列表
#     catalog_jsonlist = []
#     # 转换格式并存储
#     for each in catalog_list:
#         catalog_jsonlist.append(dict(each))
#     # 转换成json数组
#     catalog_json = json.dumps(catalog_jsonlist, default=str, ensure_ascii=False)
#     catalog_json = json.loads(catalog_json)
#     # 返回数组
#     return catalog_json
# def search_book_state(book_ISBN):
#     # 查询并返回一个列表，列表包括全部对象
#     catalog_list = Catalog.query.filter(Catalog.book_ISBN == book_ISBN)
#     state_list = []
#     #将书的状态单独提取
#     for each in catalog_list:
#         state_list.append(each.book_state)
#     return state_list