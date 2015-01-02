from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
admin.autodiscover()
from books.views import *
from jsonrpc import jsonrpc_site
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'book', BookViewSet)


urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	(r'^register/$',register_page),
	(r'^login/$','django.contrib.auth.views.login'),
	#(r'^json/$', jsonrpc_site.dispatch, name='jsonrpc_mountpoint'),
	(r'^/?$', index),
	(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	(r'^add_book/$', add_book_rpc),
	(r'^add_category/$', add_category_rpc),
	(r'^contact/$', contact),
	(r'^search/$', search),
	(r'^basket/$', basket),
	(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	(r'^rest/', include(router.urls)),
	(r'^admin_page/$',admin_page),
	(r'^save_book/$',edit_book_page_rpc),
	(r'^delete_book/$',delete_book_page_rpc),
	(r'^category/$',category),
	
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (r'^json/', jsonrpc_site.dispatch))

#urlpatterns = [
#    url(r'^', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#]
