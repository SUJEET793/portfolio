from django.http import HttpResponse
from django.shortcuts import render
from .models import Job

# Create your views here.
def sujeet(request):
    jobs=Job.objects
    return render(request,'sujeet.html',{'jobs':jobs})