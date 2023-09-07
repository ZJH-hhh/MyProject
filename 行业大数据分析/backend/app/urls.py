
from django.urls import path
from app.views.test import test
from app.views.assess import assess
from app.views.typeScore import typeScore

urlpatterns = [
    path('test/', test, name='test'),
    path('assess/', assess, name='assess'),
    path('typescore/', typeScore, name='typescore'),
]
