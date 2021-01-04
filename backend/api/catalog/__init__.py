from flask import Blueprint
catalog_blu = Blueprint('catalog_blu', __name__)
from .controller import catalog_controller  # 为了解释时蓝图能够加载到数据！！！ 而且不可以使用通配符*！！！
from .models import catalog_model
