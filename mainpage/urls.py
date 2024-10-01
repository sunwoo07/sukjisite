from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('privacy_policy', views.privacypolicy, name='privacy_policy'),
]
