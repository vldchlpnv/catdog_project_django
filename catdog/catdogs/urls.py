from django.urls import path
from . import views    # если импортируем из текущего модуля(файла то вместо названия пишем точку '.')

urlpatterns = [
    path('', views.index), # оставив тут пустую стрку в поле суффикса url адреса мы делаем ее главной (маршрут отвечает за главную страницу)
    path('breed_of_cats/', views.breed_of_cats),    # страница список пород кошек
    path('breed_of_dogs/', views.breed_of_dogs),    # страница список пород собак
    path('example_for_tag/', views.exapmle_for_tag) # '/' на конце это слеш который будет так же отображен в ссылке
]