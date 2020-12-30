# @Author  : Edlison
# @Date    : 12/30/20 10:50


class SystemResult:
    def __init__(self):
        self.status = None
        self.msg = None
        self.data = None

    def ok(self, msg='success'):
        self.status = 0
        self.msg = msg
        return self

    def error(self, msg='error'):
        self.status = 1
        self.msg = msg
        return self

    def set_data(self, data):
        self.data = data

    def keys(self):
        return ['status', 'msg', 'data']

    def __getitem__(self, item):
        return getattr(self, item)
