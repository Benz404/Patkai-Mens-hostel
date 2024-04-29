from django.urls import path
from . import views
#from .views import database

urlpatterns=[
    path('login', views.login_user ,name='login'),
    path('logout', views.logout_user ,name='logout'),
    path('superpage', views.superpage ,name='superpage'),
    path('delete/<int:pk>', views.delete ,name='delete'),
    path('delete_fees/<int:pk>', views.delete_fees ,name='delete_fees'),
    path('edit/<int:pk>', views.edit ,name='edit'),
    path('payment_students_list', views.payment_student_list ,name='payment_students_list'),
    path('payment/<int:pk>', views.payment_form ,name='payment_form'),
    path('payment_history/<int:pk>', views.fees_history ,name='fees_history'),
    path('visualisation',views.visualisation,name="visualisation"),
    path('reciept/<int:pk>', views.reciept ,name='reciept'),
]