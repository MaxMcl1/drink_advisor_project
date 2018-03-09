from django.conf.urls import url
from drinkadvisor import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
