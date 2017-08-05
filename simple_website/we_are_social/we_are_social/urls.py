
from django.conf.urls import url, include
from django.contrib import admin
from hello import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^$', views.get_index),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
]
