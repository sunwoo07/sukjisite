from django.urls import path

from accountapp import views

urlpatterns = [
    path('helloworld/', views.helloworld, name='helloworld'),
    path('index/', views.index, name='index')
]
