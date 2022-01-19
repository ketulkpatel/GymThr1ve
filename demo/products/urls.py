from django.urls import path
from products import views

urlpatterns = [

    path('', views.IndexView.as_view(), name="index"),
    path('home/', views.HomeView.as_view(), name="home"),

    path('category/', views.CategoryView.as_view(), name="category"),
    path('productDetail/<int:id>', views.ProductDetail.as_view(), name="productDetail"),
    path('productDetail/<int:id>/add_cart/', views.AddCartView.as_view(), name="add_Cart"),
    path('listproducts/<int:id>', views.ListProducts.as_view(), name="listproducts"),
    path('productList/<str:process>/', views.ProductSearchView.as_view(), name="searchview"),
    path('category/add_Cart/', views.AddCartView.as_view(), name="add_Cart"),
    path('home/add_Cart/', views.AddCartView.as_view(), name="add_Cart"),
    path('add_Cart/', views.AddCartView.as_view(), name="add_Cart"),
    path('Checkout/', views.CheckoutView.as_view(), name="Checkout"),
    path('sendmail/', views.SendMailView.as_view(), name="sendmail"),
    path('<str:process>/', views.SearchView.as_view(), name="homesearchview"),
    
    

]
