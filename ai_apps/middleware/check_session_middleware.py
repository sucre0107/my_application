from django.shortcuts import redirect

class CheckUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 检查请求的路径是否以 '/ai_apps/' 开头
        if request.path.startswith('/ai_apps/') and request.path != '/ai_apps/auth/login/' and request.path != '/ai_apps/auth/':
            # 在这里你可以访问request.session
            if 'user_id' not in request.session:
                return redirect('login_page')

        response = self.get_response(request)
        return response
