# @Author  : Edlison
# @Date    : 12/28/20 18:07
from flask import Blueprint
user_blu = Blueprint('user_blu', __name__)
from .controller import user_controller  # 为了解释时蓝图能够加载到数据！！！ 而且不可以使用通配符*！！！
from .models import user_model, role_model  # 初始化相应表的连接
