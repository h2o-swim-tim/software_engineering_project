from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.cal_index,name='cal_index')

]
