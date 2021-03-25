from django.urls import path

from . import views

'''urlpatterns = [
    path("register", views.register, name ="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout, name = "logout")
]'''

'''urlpatterns= [
    path("emp",views.emp,name='emp'),
    path("view",views.view,name='view'),
    path("delete",views.delete,name="delete"),
    path("edit",views.edit,name='edit'),
]'''


urlpatterns= [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]
    














































































































































'''from django.contrib import admin  
from django.urls import path  
from Employee import views  
urlpatterns = [  
    #path('admin/', admin.site.urls),  
    path('employee/', views.employee),  
    path('show/',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    #path('delete/<int:id>', views.destroy), 
]'''