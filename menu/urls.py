from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu_page, name='catalog'),
    path('<path:slug>/', views.category_page, name='catalog_category'),
]
