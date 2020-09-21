from django.conf.urls import url

from userApp import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^get_code/', views.get_code, name='get_code'),
    url(r'^check_name/', views.check_name, name='check_name'),
    url(r'^account/',views.account),
    # url(r'^sendemail', views.sendemail)
    url(r'^logout/', views.logout, name='logout')
]