from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TAS_Ksiegarnia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
	url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', 'books.views.index'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


