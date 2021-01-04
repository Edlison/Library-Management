import json
from backend.api.interview.models.interview_model import Interview
from backend.api import db


def insert(book_ISBN,book_name,book_price,book_author,book_public_company,book_num,user_id):
    #查询是否有重复推荐
    interview_list =  Interview.query.filter(Interview.book_ISBN == book_ISBN)
    #对清单内数量数目计数
    count = Interview.query.filter().count()
    #书目第一次被推荐
    if interview_list == ():
        interview_id = count + 1
        interview = Interview(interview_id=interview_id,
                              book_ISBN=book_ISBN,
                              book_name=book_name,
                              book_price=book_price,
                              book_author=book_author,
                              book_public_company=book_public_company,
                              book_num=book_num,
                              user_id=user_id)
        db.session.add(interview)
        db.session.commit()
    #已经有过推荐
    else :
        #查找推荐记录
        book = Interview.query.filter(Interview.book_ISBN == book_ISBN).all()
        #是否为同一个人重复推荐
        flag = 1
        for each in book:
            if each.user_id == int(user_id):
                if book_num == None:
                    book_num = 0
                each.book_num = each.book_num + int(book_num)
                db.session.commit()
                flag = 0
                break
        if  flag :
            interview_id = count + 1
            interview = Interview(interview_id=interview_id,
                                  book_ISBN=book_ISBN,
                                  book_name=book_name,
                                  book_price=book_price,
                                  book_author=book_author,
                                  book_public_company=book_public_company,
                                  book_num=book_num,
                                  user_id=user_id)
            db.session.add(interview)
            db.session.commit()


def search():
    #要汇总的
    #获得采访清单内所有的内容
    interview_list =  Interview.query.all()
    #用来存储转换成json格式的列表
    interview_jsonlist = []
    interview_ISBNlist = []
    #转换格式并汇总存储
    for each in interview_list:
        if each.book_ISBN in interview_ISBNlist:
            book_num = interview_jsonlist[interview_ISBNlist.index(each.book_ISBN)].get("book_num")
            book_num = book_num + each.book_num
            interview_jsonlist[interview_ISBNlist.index(each.book_ISBN)].update({"book_num" : book_num})
        else:
            interview_ISBNlist.append(each.book_ISBN)
            interview_jsonlist.append(dict(each))
    #转换成json数组
    interview_json = json.dumps(interview_jsonlist,default=str,ensure_ascii=False)
    interview_json = json.loads(interview_json)
    #返回数组
    return interview_json
