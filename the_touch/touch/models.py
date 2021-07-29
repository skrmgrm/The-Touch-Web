from django.db import models
from django.db.models.expressions import OrderBy
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse


# Create your models here.


class PublishedManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = AutoSlugField(
        populate_from=['title'], max_length=250, unique_for_date='publish')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_posts')
    author = models.CharField(max_length=250, blank=True, null=True)
    graphics = models.CharField(max_length=250, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='published')
    published = PublishedManger()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('touch:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title
