from django.shortcuts import render
from django.http import HttpResponse 
def index(request):
    return HttpResponse("Index Page")
def posts(request):
    return HttpResponse("Posts page")
def post_detail(request):
    return HttpResponse("Post detail page")
