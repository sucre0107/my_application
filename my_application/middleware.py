from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class SimpleAuthMiddleware(MiddlewareMixin):
    # 查找get请求中是否有auth_code参数，如果没有则返回403
    # return None表示继续执行后续的中间件和视图
    def process_request(self, request):
        auth_code = request.GET.get("auth_code")
        if auth_code != "W5u3BVSxYtbjB7":
            return HttpResponseForbidden()
        return None