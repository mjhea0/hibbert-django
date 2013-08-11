from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

from django_test.forms import ContactForm1, ContactForm2, ContactForm3
from django_test.views import ContactWizard

urlpatterns = patterns('',
	(r'^articles/', include('article.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.articles'),
    (r'^accounts/', include('userprofile.urls')),


    # user auth urls
    url(r'^accounts/login/$', 'django_test.views.login'),
    url(r'^accounts/auth/$', 'django_test.views.auth_view'),
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid_login/$', 'django_test.views.invalid_login'),

    # user registration
    url(r'^accounts/register/$', 'django_test.views.register_user'),
    url(r'^accounts/register_success/$', 'django_test.views.register_success'),
    
    # contact form wizard
    url(r'^contact/$', ContactWizard.as_view([ContactForm1,ContactForm2,ContactForm3])),
)

if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()