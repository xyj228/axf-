from django.conf.urls import url

from orderApp import views

urlpatterns = [
    url(r'^order_info/', views.order_info),
    url(r'^make_order/', views.make_order)
]
