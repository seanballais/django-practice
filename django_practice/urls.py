from django.conf.urls import include, url
from django.contrib import admin
from django_practice.views import hello
from django_practice.views import current_datetime
from django_practice.views import hours_ahead

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead)
]
