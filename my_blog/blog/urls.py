from django.urls import path
from . import views 

urlpatterns = [
    path("",views.home,name="home-page"),
    path("posts",views.posts, name="posts-page"),
    path("posts,<slug>",views.post_detail, name="post-detail"),
]
