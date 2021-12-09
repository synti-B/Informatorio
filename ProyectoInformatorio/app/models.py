from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    author= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title= models.CharField(max_length=260)
    content= models.TextField()
    img= models.ImageField(null=True, blank=True, upload_to='img', help_text='Seleccione una imagen para mostrar')
    created_on= models.DateTimeField(default=timezone.now)
    last_modified= models.DateTimeField(auto_now=True)
    published_date= models.DateTimeField(null=True, blank=True)
    categorias= models.ManyToManyField('category', related_name='posts')

    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        #return reverse('apps.blog:blog_detail', args=(str(self.id)))
        return reverse("apps.blog:blog_detail",kwargs={'id':self.pk})


    def __str__(self):
        return self.title
    
    