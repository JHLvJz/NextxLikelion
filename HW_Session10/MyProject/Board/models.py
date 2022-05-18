from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    viewcount = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    #cascade = article객체가 삭제될 때, 이를 참조하던 것들도 같이 삭제되도록
    def __str__(self):
        return self.content