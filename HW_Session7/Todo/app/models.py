from django.db import models

# Create your models here.
class Post(models.Model): #Q왜 매개변수 이거지
    title = models.CharField(max_length=200) #Q왜 models.으로 접근하지
    content = models.TextField()
    deadline = models.DateField()

    def __str__(self): #Q이거 공부하기
        return self.title
