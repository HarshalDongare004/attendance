"""myAttendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from * import views
from Employee import views

'''urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('attendance.urls')),
    path('company/',include('company.urls')),
    #path('Employee/', include('Employee.urls')),
    path('emp/',views.emp),
    path('view/',views.view),
    path ('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    
    #url(r'^api-auth/',include('rest-framework.urls',namespace='rest_framework')),
   # url(r'^api/', include(router.urls)),

]

#urlpatterns = urlpatterns + '''


urlpatterns = [
     path('admin/', admin.site.urls),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('Employee/', include('Employee.urls'))
]