from django.urls import path
from. import views

app_name = 'produto'
urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos, name='produtos'),
    path('car/', views.car, name='car'),
    path('contato/', views.contato, name='contato'),
]
