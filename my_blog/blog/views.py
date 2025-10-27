from django.shortcuts import render

def home(request):

    return render(request,"blog/home.html")

def posts(request):

    return render(request,"blog/all-posts.html")


def post_detail(request):
    pass
