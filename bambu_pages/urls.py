from django.conf.urls import patterns, url
from bambu_pages.views import page
from django.conf import settings

if 'bambu_bootstrap' in settings.INSTALLED_APPS:
    from bambu_bootstrap.decorators import body_classes
else:
    def body_classes(view, *classes):
        return view

urlpatterns = patterns('',
    url(r'^(?P<slug>[\/\w-]+)/$', body_classes(page, 'page'), name = 'page')
)