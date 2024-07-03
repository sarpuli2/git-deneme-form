from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Post(models.Model):
    #user= models.ForeignKey('auth.User', verbase_name='Yazar')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar' ,related_name='posts')
    title = models.CharField(max_length=120, verbose_name='Başlık')
    content = RichTextUploadingField(verbose_name='İçerik')  # RichTextField yerine RichTextUploadingField kullanıldı
    publishing_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug(self.title)
        return super().save(*args, **kwargs)

    def generate_unique_slug(self, title):
        slug = slugify(title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    class Meta:
        ordering = ['-publishing_date', 'id']

class Comment(models.Model):

    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, verbose_name='isim')
    content = models.TextField(verbose_name='Yorum')

    created_date = models.DateTimeField(auto_now_add=True)

class iletisim(models.Model):

    post = models.ForeignKey('post.Post', related_name='iletisim', on_delete=models.CASCADE)

    name = models.CharField(max_length=200, verbose_name='isim')
    content = models.TextField(verbose_name='Yorum')

    created_date = models.DateTimeField(auto_now_add=True)



