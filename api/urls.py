from django.urls import path
from . import views

urlpatterns = [
    path('product-list', views.list_products),
    path('product-detail/<int:id>/', views.product_detail),
    path('categorys', views.category_list),
    path('category-detail/<str:slug>/', views.category_detail),
    path('login', views.log_in),
    path('register', views.register_user),
    path('list-users', views.list_users),
    # path('salom', views.salomlash)
]