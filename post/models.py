from django.db import models

# Create your models here.


class Post(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Title')
    metin = models.TextField(verbose_name='Content')
    yayimlanma_tarihi = models.DateTimeField(verbose_name='Published Date')

    def __str__(self):
        return self.baslik