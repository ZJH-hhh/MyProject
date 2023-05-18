from rest_framework.views import APIView
from rest_framework. response import Response
from rest_framework.permissions import IsAuthenticated
from app.models.UserInfo import Users
from app.models.jobs import Jobs


class InfoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id', 1))
            user = Users.objects.get(user_id=user_id)
            # user = Jobs.objects.get(id=user_id)
            # print(user)
            return Response({
                # 'id': user.id,
                'username': user.user.username,
                'photo': user.photo,
            })
        except:
            return Response({
                'result': "输入参数错误",
            })

# from rest_framework import viewsets

# from app.models.UserInfo import User
# from app.serializer import UsersSerializer


# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UsersSerializer
