from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(editable=False, max_length=110)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('tag', kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=110)
    slug = models.SlugField(default='', editable=False, max_length=110)
    tag = models.ForeignKey(Tag, default=1, on_delete=models.PROTECT)
    content = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=110)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('blog-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            value = self.title
            self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)