from django.conf.urls import url

from mainApp import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^market/', views.market, name='market'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^mine/', views.mine, name='mine'),
    url(r'^addCart/', views.addCart),
    url(r'^subCart/', views.subCart),
    url(r'^changeSingle/', views.changeSingle),
    url(r'^allSelect/', views.allSelect),
    url(r'^sub/', views.sub),
    url(r'^add/', views.add),
    url(r'^totalPrice', views.totalPrice)

]
