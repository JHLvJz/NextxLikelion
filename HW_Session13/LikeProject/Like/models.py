from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles'
    )
    #Foreignkey복습 - 매개변수: 참조할 테이블, 개체관계에서 사용할 이름, 매체삭제 시 수행할 동작
    #related_name = 개체 관계시 사용할 이름 // on_delete = 개체 삭제 시 수행할 동작 (게시물 삭제될 때, 댓글은 어떻게?)
    #models.CASCADE = 삭제할 때 foreignkey를 포함하는 행도 함께 삭제
    #참고(https://076923.github.io/posts/Python-Django-11/)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    
    #related_name 지정시 유의사항 참고(https://fabl1106.github.io/django/2019/05/27/Django-26.-%EC%9E%A5%EA%B3%A0-related_name-%EC%84%A4%EC%A0%95%EB%B0%A9%EB%B2%95.html)

class Like(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='likes'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes'
    )

class Scrap(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='scraps'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='scrpas'
    )
