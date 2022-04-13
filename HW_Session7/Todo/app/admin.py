from django.contrib import admin
from .models import Post #models.py에 내가 만들어둔 Post라는 class를 import

# Register your models here.
admin.site.register(Post) #Q이거 무슨 기능일까요
