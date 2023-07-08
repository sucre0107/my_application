# 封装一个响应类
# 将数据封装到一个对象中，这样就可以在视图函数中直接返回对象，而不用再去构造响应体了
class BaseResponse(object):
    def __init__(self, status=False, detail=None, data=None):
        self.status = status
        self.detail = detail
        self.data = data

    @property
    def dict(self):
        return self.__dict__