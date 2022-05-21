from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
#내가 정의한 모델을 관리자 페이지에서 볼 수 있도록