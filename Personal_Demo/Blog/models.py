# coding:utf-8
from django.db import models
from django.contrib.admin.widgets import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.


class UserInfo(models.Model):
    account = models.CharField('account', max_length=60)
    passwd = models.CharField('passwd', max_length=100)

    def __str__(self):
        return self.account


class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签 Tag 也比较简单，和 Category 一样
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章的数据库表
    """

    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Blog:detail', kwargs={'pk': self.pk})

    def increase_view(self):
        self.views += 1
        self.save(update_fields=['views'])
