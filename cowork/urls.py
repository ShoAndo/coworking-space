from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # 一覧画面
    path('', views.index, name='index'),
    path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
    path('accounts/logout/', views.Logout.as_view(), name='logout'),
    path('reserve/<int:seat_id>/', views.reserve, name="reserve"),
]