from django.conf.urls import url
from drinkadvisor import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^drinks/', views.drinks, name='drinks'),
    url(r'^sugar_free/', views.sugar_free, name='sugar_free'),
    
]
