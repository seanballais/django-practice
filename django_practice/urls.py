from django.conf.urls import include, url
from django.contrib import admin
from django_practice.views import hello
from django_practice.views import current_datetime
from django_practice.views import hours_ahead
from django_practice.views import display_meta
from django_practice.views import contact
from books import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^meta/$', display_meta),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact)
]
