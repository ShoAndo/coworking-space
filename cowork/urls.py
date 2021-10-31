from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # 一覧画面
    path('', views.index, name='index'),
    path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
]