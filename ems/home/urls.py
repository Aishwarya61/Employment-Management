from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('home/',views.index,name='index'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path('remove_emp/',views.remove_emp,name='remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp),
    path('all_emp/',views.all_emp,name='all_emp'),
    path('filter_emp/',views.filter_emp,name='filter_emp')
    
]