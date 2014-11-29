from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^register/$','books.views.register_page'),
	(r'^login/$','django.contrib.auth.views.login'),
	(r'^/?$', 'books.views.index'),
	(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	(r'^add_book/$', 'books.views.add_book'),
	(r'^add_category/$', 'books.views.add_category'),
	(r'^contact/$', 'books.views.contact'),
	(r'^search/$', 'books.views.search'),
	(r'^basket/$', 'books.views.basket'),
	
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


