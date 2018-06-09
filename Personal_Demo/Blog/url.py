from django.conf.urls import url


urlpatterns = [
    url(r'^login/', 'Blog.views.login', name='login'),
    url(r'^logins/', 'Blog.views.logins', name='logins'),
    url(r'^index/', 'Blog.views.index', name='index'),

]
