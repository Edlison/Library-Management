from flask import Blueprint
interview_blu = Blueprint('interview_blu', __name__)
from .controller import interview_controller  # 为了解释时蓝图能够加载到数据！！！ 而且不可以使用通配符*！！！
from .models import interview_model
