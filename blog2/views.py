from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_blog2(request):
    return HttpResponse("Hello, blog2!")