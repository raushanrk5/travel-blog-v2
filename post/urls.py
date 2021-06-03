from django.contrib import admin
from django.urls import path
from django.conf.urls import handler400, handler500
from . import views
app_name = "post"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.add_article, name="addarticle"),
    path('post/<slug:slug>/', views.detail, name="detail"),
    path('update/<slug:slug>', views.update_article, name="update"),
    path('delete/<slug:slug>', views.delete_article, name="delete"),
    path('', views.articles, name="articles"),
    path('<slug:slug>', views.articles, name="articles"),
    path('comment/<slug:slug>', views.add_comment, name="comment"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
]
