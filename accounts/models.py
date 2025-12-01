from django.db import models

# Create your models here.


class Contact(models.Model):

    name = models.CharField(max_length=200, verbose_name='Isim')
    last_name = models.CharField(max_length=200, verbose_name='Soyisim')
    content = models.TextField(verbose_name='Yorum')
    email = models.CharField(max_length=40,verbose_name='EmailAdress')
    created_date = models.DateTimeField(auto_now_add=True)