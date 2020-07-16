from django.urls import path, include
from dataHolder.views import *

app_name = 'dataHolder'


urlpatterns = [
    path('', index, name='index'),
    path('week/', week_stat, name='week_stat'),
    path('week2014/', week_stat2014, name='week_stat2014'),
    path('week2015/', week_stat2015, name='week_stat2015'),
    path('week2016/', week_stat2016, name='week_stat2016'),
    path('week2017/', week_stat2017, name='week_stat2017'),
    path('week2018/', week_stat2018, name='week_stat2018'),
    path('week2019/', week_stat2019, name='week_stat2019'),
    path('week2020/', week_stat2020, name='week_stat2020'),
    path('mood/', mood, name='mood'),
]
