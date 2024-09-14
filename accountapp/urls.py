from django.urls import path

from accountapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('helloworld/', views.helloworld, name='helloworld'),
]
