
from django.shortcuts import render
from .models import *

# Create your views here.
def company_name(request):
    #official_info = OfficialInfo.objects.all()
    #context = {
    #    "official_info": official_info
    #}'''
    return render(request, "company_name.html")
