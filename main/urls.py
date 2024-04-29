from django.urls import path
from . import views
#from .views import database

urlpatterns=[
    path('', views.index ,name='index'),
    path('students_list', views.students_list ,name='students_list'),
    path('students_detail/<int:pk>', views.the_student ,name='students_detail'),
    path('students_admit_form',views.students_admit_form,name='students_admit_form'),
    path('author', views.author ,name='author'),
]