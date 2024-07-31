from django.urls import path
from . import views
from .views import PostListView


urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),

    path('', PostListView.as_view(), name="blog-home"),
    path('post-new/', PostCreateView.as_view(), name="blog-new"),

]
    #path('about/', views.about, name="blog-about"),