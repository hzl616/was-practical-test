from django.db import models


class Article(models.Model):
    article_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
