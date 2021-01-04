# 图书管理系统 Library-Management

**前端**[VUE](frontend) by [Elkmiao](https://github.com/Elkmiao)

**后端**[FLASK](backend) by [Edlison](https://github.com/Edlison) & [ad-zt](https://github.com/ad-zt)

## Backend

### Quick Start

1. 使用pip安装依赖  
   `pip install -r requirment.txt`

2. 启动项目  
   `python application.py runserver -h 0.0.0.0 -p 5000`

3. 请求接口

- [用户管理子系统](./backend/api/user)

  |url|content|
    |----|----|
  |/api/user/login|用户登陆|
  |/api/user/get_info|获取用户信息|

- [采访子系统](./backend/api/interview)

  |url|content|
    |----|----|
  |/api/interview/addinterviews|添加采访记录|
  |/api/interview/showinterviews|显示采访记录|

- [编目子系统](./backend/api/catalog)

  |url|content|
    |----|----|
  |/api/catalog/addcatalog_one|添加一条编目信息|
  |/api/catalog/addcatalog_list|添加多条编目信息|
  |/api/catalog/show_return_catalog|显示编目|
  |/api/catalog/showcatalog|显示编目|
  |/api/catalog/catalog_search_ISBN|查找编目信息|

- [流通子系统](./backend/api/circulation)

  |url|content|
    |----|----|
  |/api/circulation/borrow|借阅|
  |/api/circulation/reserve|预约|
  |/api/circulation/get_borrow|获取用户借阅信息|
  |/api/circulation/get_resr|获取用户预约信息|
  |/api/circulation/renew|续借|
  |/api/circulation/ret_book|还书|
  |/api/circulation/canc_resr|取消预约|
  |/api/circulation/resr2borr|预约转借阅|
  |/api/circulation/get_book|获取某本书的详细信息|
  |/api/circulation/get_all_books|获取全部馆藏信息|

----
APIs: http://rap2.taobao.org/repository/editor?id=274105

GitRepo: https://github.com/Edlison/Library-Management
