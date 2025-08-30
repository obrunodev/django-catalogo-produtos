from django.urls import path
from apps.products import views

app_name = 'products'
urlpatterns = [
    path('create/', views.product_create, name='create'),
    path('', views.product_list, name='list'),
    path('<int:product_id>/delete/', views.product_delete, name='delete'),
    path('<str:product_slug>/update/', views.product_update, name='update'),
    path('marketplace/', views.product_marketplace, name='marketplace'),
    path('detail/<str:product_slug>/', views.product_detail, name='detail'),
]
