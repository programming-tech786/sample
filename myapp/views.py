from django.shortcuts import render
from .models import *
# Create your views here.
def Sample1(request):
	return render(request,'myapp/sample1.html')