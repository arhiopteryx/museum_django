from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),  # Страница входа
    path('register/', views.register, name='register'),  # Страница регистрации
    path('exhibits/', views.exhibit_list, name='exhibit_list'),  # Список экспонатов
    path('exhibit/<int:pk>/', views.exhibit_detail, name='exhibit_detail'),  # Подробности по экспонату
    path('exhibit/new/', views.exhibit_create, name='exhibit_create'),  # Создание экспоната
    path('exhibit/<int:pk>/edit/', views.exhibit_edit, name='exhibit_edit'),  # Редактирование экспоната
    path('exhibit/<int:pk>/delete/', views.exhibit_delete, name='exhibit_delete'),  # Удаление экспоната
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Выход
]