from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


class RegisterView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        if not username or not password:
            return Response({
                'result': '用户名或密码不能为空',
            })
        if password != password_confirm:
            return Response({
                'result': '密码不一致',
            })
        if User.objects.filter(username=username).exists():
            return Response({
                'result': '用户名已存在',
            })
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return Response({
            'result': 'success',
        })
