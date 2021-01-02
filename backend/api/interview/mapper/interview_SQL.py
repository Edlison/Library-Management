from backend.api.interview.models.interview_model import Interview
from backend.api import db
import json

def insert(book_ISBN,book_name,book_price,book_author,book_public_company,book_num,user_id):
    #查询是否有重复推荐
    interview_list =  Interview.query.filter_by(Interview.book_ISBN == book_ISBN)
    #对清单内数量数目计数
    count = Interview.query.all().count()
    #书目第一次被推荐
    if interview_list == ():
        interview_id = count + 1
        interview = Interview(interview_id,
                              book_ISBN,
                              book_name,
                              book_price,
                              book_author,
                              book_public_company,
                              book_num,
                              user_id)
        db.session.add(interview)
    #已经有过推荐
    else :
        #查找推荐记录
        book = Interview.query.filter_by(Interview.book_ISBN == book_ISBN)
        #是否为同一个人重复推荐
        flag = 1
        for each in book:
            if each.user_id == user_id:
                if book_num == None:
                    book_num = 0
                each.book_num = each.book_num+book_num
                flag = 0
                break
        if  flag :
            interview_id = count + 1
            interview = Interview(interview_id,
                                  book_ISBN,
                                  book_name,
                                  book_price,
                                  book_author,
                                  book_public_company,
                                  book_num,
                                  user_id)
            db.session.add(interview)
    db.session.commit()


def search():
    #获得采访清单内所有的内容
    interview_list =  Interview.query.all()
    #用来存储转换成json格式的列表
    interview_jsonlist = []
    #转换格式并存储
    for each in interview_list:
        interview_jsonlist.append(dict(each))
    #转换成json数组
    interview_json = json.dumps(interview_jsonlist,ensure_ascii=False)
    #返回数组
    return interview_json
