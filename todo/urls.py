from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('update/<int:employee_id>/', views.update, name='update'),
    path('delete/<int:employee_id>/', views.delete, name='delete'),

]
