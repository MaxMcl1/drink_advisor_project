from django.conf.urls import url
from drinkadvisor import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^drinks/', views.drinks, name='drinks'),
    url(r'^sugar_free/', views.sugar_free, name='sugar_free'),
    url(r'^energy_drinks/', views.energy_drinks, name='energy_drinks'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^add_drink/$', views.add_drink, name='add_drink'),
    url(r'^drink/(?P<drink_name_slug>[\w\-]+)/$',
        views.show_drink, name='show_drink'),

    
]
