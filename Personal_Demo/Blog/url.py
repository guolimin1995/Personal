import views
from django.conf.urls import url


app_name = "Blog"

urlpatterns = [
    url(r'^login/', 'Blog.views.login', name='login'),
    # url(r'^logins/', 'Blog.views.logins', name='logins'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^semantic/', views.semantic, name='semantic'),
]
