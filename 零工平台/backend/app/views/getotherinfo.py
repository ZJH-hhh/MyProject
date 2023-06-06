from rest_framework.views import APIView
from rest_framework. response import Response
from django.contrib.auth.models import User


class OtherInfoView(APIView):

    def get(self, request):
        try:
            print(request.GET)
            username = request.GET.get('username')
            user = User.objects.get(username=username)
            return Response({
                'username': user.username,
                'email': user.email,
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })
