from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Title')
    metin = models.TextField(verbose_name='Content')
    yayimlanma_tarihi = models.DateTimeField(verbose_name='Published Date', auto_now_add=True)

    def __str__(self):
        return self.baslik
    
    def get_absolute_url(self):

        return reverse('post:detail', kwargs={"id" : self.id})

        # return "/post/{}".format(self.id)

        
    def get_create_url(self):

        return reverse('post:detail')
    
        
    def get_update_url(self):

        return reverse('post:update', kwargs={"id" : self.id})
    
        
    def get_delete_url(self):

        return reverse('post:delete', kwargs={"id" : self.id})