

from django.db import models 
from datetime import datetime, timedelta 
class Employee(models.Model):  
     
    employee_name = models.CharField(max_length=100, null=True)  
    mobile_number = models.CharField(max_length=200, null= True)
    #address = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)  
    #date = models.DateTimeField(default=datetime.now()+ timedelta(days =30))
    
    def __str__(self):
        return self.employee_name
   
    class Meta:  
        db_table = "Employee"

























































































































































































'''from django.db import models

# Create your models here.
class EmployeeInfo(models.Model):
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    Employee_id = models.IntegerField()
    

    #def __str__(self):
       # return self.first_name'''


'''class OfficialInfo(models.Model):
    official_register_number = models.CharField(max_length=20)
    official_register_date = models.DateField()

    def __str__(self):
        return self.official_register_number'''


'''class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    another_fullname = models.CharField(max_length=100)
    employee_id = models.IntegerField()'''
   
   # def __str__(self):
  #      return self.full_name
