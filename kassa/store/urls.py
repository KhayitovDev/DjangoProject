from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard, name='mainDashboard' ),
    path('kassa/', views.Kassa, name='kassa'),
    path('add/', views.add, name='addElement'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]