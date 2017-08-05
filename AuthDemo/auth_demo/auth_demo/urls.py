
from django.conf.urls import url
from django.contrib import admin
from hello import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.get_index, name='index'),
url(r'^register/$', accounts_views.register, name='register'),
]
