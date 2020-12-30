# @Author  : Edlison
# @Date    : 12/28/20 18:10
from backend.api.user import user_blu
from flask import request, jsonify, session, make_response
import json
from backend.api import db
from backend.api.user.models.user_model import User
from backend.result.system_result import SystemResult


@user_blu.route('/edlison', methods=['GET'])
def user_home():
    print('request success')
    return 'hello'


@user_blu.route('/login', methods=['POST'])
def login():
    data = request.get_data()
    print('data1:',data)
    data = json.loads(data)
    data = data['data']
    session['username']=data['username']
    print(session.get('username'))
    return jsonify(data)


@user_blu.route('/create', methods=['POST'])
def create():
    db.create_all()
    return make_response('ok')


@user_blu.route('/insert', methods=['POST'])
def insert():
    admin = User('admin', 'admin123')
    edlison = User('edlison', 'qwer1234!')
    admin.set_role(1)
    edlison.set_role(2)
    db.session.add(admin)
    db.session.add(edlison)
    db.session.commit()
    return make_response('ok')


@user_blu.route('/getRes', methods=['POST'])
def getRes():
    users = User.query.all()
    res = SystemResult().ok()
    res.set_data([dict(users[0]), dict(users[1])])
    print(res)
    return jsonify(dict(res))
