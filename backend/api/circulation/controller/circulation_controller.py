# @Author  : Edlison
# @Date    : 12/31/20 18:32
from backend.api.circulation import cir_blu
from backend.api import db
from flask import make_response
# TODO 写接口和文档


@cir_blu.route('/borrow', methods=['POST'])
def borrow():  # TODO 借书流程
    ...


@cir_blu.route('/reserve', methods=['POST'])
def reserve():  # TODO 预约流程
    ...