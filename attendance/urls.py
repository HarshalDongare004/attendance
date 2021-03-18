#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('attendance',views.attendance, name='attendance')
    #path('user_attendance',views.user_attendance, name='user_attendance')
    #path('attendance_by_user',views.attendance_by_user, name='attendance_by_user')
    #path('signup',views.signup,name='signup')
    #path('signup_by_iso_date',views.signup_by_iso_date, name='signup_by_iso_date')
    path('', views.home, name='home'),
    #path('add', views.add, name='add'),
    path('student_list',)
]


