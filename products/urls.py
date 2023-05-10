from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_list/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('add_order/', views.CreateOrderView.as_view(), name='create_order'),
    path('product_jacket/', views.ProductJacketView.as_view(), name='product_jacket'),
    path('product_boots/', views.ProductBootsView.as_view(), name='product_boots'),
    path('product_shirt/', views.ProductShirtView.as_view(), name='product_shirt'),
    path('product_cap/', views.ProductCapView.as_view(), name='product_cap'),

]
