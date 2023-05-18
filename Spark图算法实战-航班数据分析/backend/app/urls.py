
from django.urls import path
from app.views import test, popular, airline, delay, getusa, getshortest, getimportant, getcheapest, getedges, tendelay, air_location

urlpatterns = [
    path('getdata/', test, name='test'),
    path('getpopular/', popular, name='popular'),
    path('getairline/', airline, name='airline'),
    path('getdelay/', delay, name='delay'),
    path('getusa/', getusa, name='getusa'),
    path('getshortest/', getshortest, name='getshortest'),
    path('getimportant/', getimportant, name='getimportant'),
    path('getcheapest/', getcheapest, name='getcheapest'),
    path('getedges/', getedges, name='getedges'),
    path('gettendelay/', tendelay, name='tendelay'),
    path('getairlocation/', air_location, name='air_location'),
]
