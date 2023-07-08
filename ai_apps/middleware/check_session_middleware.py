from django.shortcuts import redirect

class CheckUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 检查请求的路径是否以 '/ai_apps/' 开头
        excluded_paths = ['/ai_apps/auth/login/', '/ai_apps/auth/', '/ai_apps/auth/register/manual']
        if request.path.startswith('/ai_apps/') and request.path not in excluded_paths:
            # 在这里你可以访问request.session
            if 'user_id' not in request.session:
                return redirect('login_page')

        response = self.get_response(request)
        return response
