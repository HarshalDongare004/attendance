from django.urls import path
#from company import views
from . import views

'''urlpatterns = [
    path('company', views.company_name, name='company_name'),
    
]'''

company_name = 'Tal crafts'
urlpatterns =[
    path('',views.company_name, name='company_name')
]
