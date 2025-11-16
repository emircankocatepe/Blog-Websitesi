from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Title')
    metin = models.TextField(verbose_name='Content')
    yayimlanma_tarihi = models.DateTimeField(verbose_name='Published Date', auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True, editable=False, max_length=130)
    def __str__(self):
        return self.baslik
    
    def get_absolute_url(self):

        return reverse('post:detail', kwargs={"slug" : self.slug})

        # return "/post/{}".format(self.id)

        
    def get_create_url(self):

        return reverse('post:detail')
    
        
    def get_update_url(self):

        return reverse('post:update', kwargs={"slug" : self.slug})
    
        
    def get_delete_url(self):

        return reverse('post:delete', kwargs={"slug" : self.slug})
    
    def get_unique_slug(self):
        slug = slugify(self.baslik.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter+=1
        return unique_slug
    
    def save(self, *args, **kwargs):
        
            #self.slug = slugify(self.baslik.replace('ı', 'i'))
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-yayimlanma_tarihi', 'id']