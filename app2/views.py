from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def v1_app2(request):
    return HttpResponse('<h1>view1 of app2</h1>')


def v2_app2(request):
    return HttpResponse('<h1>view2 of app2</h1>')