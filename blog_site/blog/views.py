from django.shortcuts import render
from django.http import HttpResponse 
def index(request):
    return render(request,'blog/index.html')
def posts(request):
    return render(request,'blog/all-posts.html')
def post_detail(request,slug):
    return render(request,"blog/post-detail.html")
