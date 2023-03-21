from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(reqest):

    return HttpResponse("Hallo,this's first project of django")