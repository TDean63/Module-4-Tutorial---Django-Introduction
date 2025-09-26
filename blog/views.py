from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def post_list(request):
    return HttpResponse("Hello from the blog home page!")