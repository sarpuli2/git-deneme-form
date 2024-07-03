
from django.contrib import admin
from django.urls import path
from .views import post_index,post_create,post_detail,post_update,post_delete,post_iletisim

app_name = 'post'

urlpatterns = [

    path('index/', post_index, name='index'),
    path('create/', post_create, name='create'),

    path('post/<slug:slug>/', post_detail, name='detail'),
    path('post/<slug:slug>/update/', post_update, name='update'),
    path('post/<slug:slug>/delete/', post_delete, name='delete'),
    path('post/<slug:slug>/iletisim/', views.post_iletisim, name='iletisim'),



]
