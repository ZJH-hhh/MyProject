from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views.jobs import JobsViewSet
# from app.views.getinfo import UsersViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.views.getinfo import InfoView


router = DefaultRouter()
router.register('jobs', JobsViewSet)
# router.register('getinfo', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getinfo/', InfoView.as_view(), name='getinfo'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
