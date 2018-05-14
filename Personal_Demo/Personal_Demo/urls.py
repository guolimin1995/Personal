from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enables the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^index/', 'Blog.views.index', name='index'),
    # url(r'^Personal_Demo/', include('Personal_Demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
