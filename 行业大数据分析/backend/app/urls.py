
from django.urls import path
from app.views.test import test
from app.views.assess import assess
from app.views.typeScore import typeScore
from app.views.CityScore import cityScore
from app.views.EduScore import eduScore
from app.views.TimePredict import timePredict

urlpatterns = [
    path('test/', test, name='test'),
    path('assess/', assess, name='assess'),
    path('typescore/', typeScore, name='typescore'),
    path('cityscore/', cityScore, name='cityscore'),
    path('eduscore/', eduScore, name='eduscore'),
    path('timepredict/', timePredict, name='timePredict'),
]
