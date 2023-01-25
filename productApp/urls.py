from django.urls import path 
from productApp import views 

urlpatterns = [
    path('listproduct/',views.listproduct,name='listproduct'),
    path('createproduct/',views.createProduct, name='createproduct'),
    path('productEdit/<int:id>/', views.editProduct, name='productEdit'),
    path('productView/<int:id>/', views.viewProduct, name='productView'),
    path('productDelete/<int:id>/', views.destroyProduct, name='productDelete'),
    path('register/',views.register, name='register'),
    path('loginuser/',views.login_user, name='login_user'),
    path('logoutuser/',views.logout_user, name='logout_user'),
]