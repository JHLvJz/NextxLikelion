"""Todo URL Configuration

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
from app import views #url과 view 연결

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"), #Q이거 표기법? 공부하기 -> 맨 앞: url요청 패턴을 적는다 / 그 뒤에 실행할 것을 적는다 (여기서는 views에 있는 home함수 실행, 이 패턴의 이름은 home -> html에서 쓴다)
    path('new/', views.new, name="new"), 
    path('detail/<int:post_pk>/', views.detail, name="detail"), #<int:post_pk> 공부하기
    path('edit/<int:post_pk>/', views.edit, name="edit"),
    path('delete/<int:post_pk>/', views.delete, name="delete"),
]
