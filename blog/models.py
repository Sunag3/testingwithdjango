from django.db import models
# Changes in Gitgit a
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)

    def __str__(self):
        return self.title
