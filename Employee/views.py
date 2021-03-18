from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import  User, auth

# Create your views here.

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credientials')
            return redirect('login')

    else:
        return render(request,'employee_login.html')



def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name= last_name)
                user.save();
                print('USER CREATED')
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'employee_registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



















































































































































'''from django.shortcuts import render, redirect  
#from employee.forms import EmployeeForm  
#from employee.models import Employee  
from . import views
# Create your views here.  
def employee(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:
        pass  
        #form = EmployeeForm()  
    return render(request,'index.html')#,{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  '''
'''def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")'''
