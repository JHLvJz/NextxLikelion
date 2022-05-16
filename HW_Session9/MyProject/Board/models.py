from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    viewcount = models.IntegerField()

    def __str__(self):
        return self.title