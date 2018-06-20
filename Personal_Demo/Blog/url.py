import views
from django.conf.urls import url


app_name = "Blog"

urlpatterns = [
    # url(r'^login/', 'Blog.views.login', name='login'),
    # url(r'^logins/', 'Blog.views.logins', name='logins'),
    url(r'^$', 'Blog.views.index', name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
