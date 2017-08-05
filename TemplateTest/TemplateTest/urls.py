from django.conf.urls import include, url
from django.contrib import admin
from sitepages import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home$',views.home_page),
     url(r'^about$',views.about_page),
    url(r'^contact$',views.contact_page),


]
