from django.shortcuts import render
from django.http import HttpResponse 
def index(request):
   return render(request,'blog/index.html')
def posts(request):
    return HttpResponse("Posts page")
def post_detail(request):
    return HttpResponse("Post detail page")
