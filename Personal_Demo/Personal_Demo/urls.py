from django.conf.urls import patterns, include, url
import xadmin
# from django.contrib import admin
# Uncomment the next two lines to enables the admin:
# from django.contrib import admin
# admin.autodiscover()
xadmin.autodiscover()
urlpatterns = [
    # Examples:

    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL}),
    url(r'', include('Blog.url', namespace='Blog')),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'', include('comments.urls', namespace='comments')),
    url(r'^xadmin/captcha', 'Blog.views.refresh_captcha', name='refresh_captcha'),
    # url(r'^Personal_Demo/', include('Personal_Demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
