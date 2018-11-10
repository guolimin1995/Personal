# coding:utf-8
from Blog.models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()


@register.assignment_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.assignment_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.assignment_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.assignment_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)