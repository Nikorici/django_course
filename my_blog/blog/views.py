from django.shortcuts import render

def home(request):

    return render(request,"blog/home.html")

def posts(request):
    pass


def post_detail(request):
    pass
