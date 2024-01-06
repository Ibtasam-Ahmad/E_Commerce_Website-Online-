from django.contrib import admin
from django.urls import path
from . import views
from shop import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about', views.about, name='about'),
    path('tracker', views.tracker, name='tracker'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
]
