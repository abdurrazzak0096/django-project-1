from django.urls import path 
from studentApp import views

urlpatterns = [
    path('show_student/', views.StudentListView.as_view(), name='list_student'),
    path('create_student/', views.StudentCreateView.as_view(), name='create_student'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('detail_student/<int:pk>/', views.StudentDetailView.as_view(), name='detail_student'),

]