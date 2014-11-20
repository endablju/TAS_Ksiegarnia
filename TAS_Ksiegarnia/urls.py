from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^register/$','books.views.register_page'),
    (r'^/?$', 'books.views.index'),
	(r'^login/$','django.contrib.auth.views.login'),
    #(r'^logout/$',logout_page),
	(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


