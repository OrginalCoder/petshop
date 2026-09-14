from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hayvonlar/', views.animal_list, name='animal_list'),
    path('hayvonlar/<int:id>/', views.animal_detail, name='animal_detail'),
    path('mahsulotlar/', views.product_list, name='product_list'),
    path('shifokorlar/', views.doctor_list, name='doctor_list'),
    path('qabul/', views.appointment_form, name='appointment_form'),
    path('qabullar/', views.appointment_list, name='appointment_list'),
    path('buyurtma/<int:product_id>/', views.order_create, name='order_create'),
    path('buyurtmalar/', views.order_list, name='order_list'),
]