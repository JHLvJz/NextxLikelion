"""LikeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Like import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    #유저로그인
    path('registration/signup', views.signup, name="signup"),
    path('registration/login', views.login, name="login"),
    path('registration/logout', views.logout, name="logout"),

    #기본
    path('', views.home, name="home"),
    path('mypage/', views.mypage, name="mypage"),
    path('new/', views.new, name="new"),
    path('detail/<int:article_pk>', views.detail, name="detail"),
    path('edit/<int:article_pk>', views.edit, name="edit"),
    path('delete/<int:article_pk>', views.delete, name="delete"),
    path('delete_comment/<int:article_pk>/<int:comment_pk>', views.delete_comment, name="delete_comment"),

    #like구현
    path('like', views.like, name="like"),

    #scrap구현
    path('scrap', views.scrap, name="scrap")
    
]
