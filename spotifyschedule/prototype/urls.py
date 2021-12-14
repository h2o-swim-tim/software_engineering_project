from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('/spotify', views.index,name='index'),
    path('', views.cal_index,name = 'cal_index'),
    path('/logout', LogoutView.as_view())
]
