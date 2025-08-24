from django.urls import path
from apps.products import views

app_name = 'products'
urlpatterns = [
    path('create/', views.product_create, name='create'),
    path('', views.product_list, name='list'),
    path('<int:product_id>/delete/', views.product_delete, name='delete'),
    path('<int:product_id>/update/', views.product_update, name='update'),
]
