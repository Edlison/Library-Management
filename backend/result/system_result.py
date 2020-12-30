# @Author  : Edlison
# @Date    : 12/30/20 10:50
from backend.api.user.models.user_model import User


class SystemResult:
    def __init__(self):
        self.status = None
        self.msg = None
        self.data = None

    def ok(self):
        self.status = 0
        self.msg = 'success'
        return self

    def set_data(self, data):
        self.data = data

    def keys(self):
        return ['status', 'msg', 'data']

    def __getitem__(self, item):
        return getattr(self, item)

res = SystemResult().ok()

admin = User('admin', 'admin123')
edlison = User('edlison', 'qwer1234!')
admin.set_role(1)
edlison.set_role(2)
data = [dict(admin), dict(edlison)]
print('data', data)
res.set_data(data)
print('res', res)
