from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from users.views import notifications

urlpatterns = [
    # Static pages
    path('about/', views.about, name="blog-about"),
    path('contact/', views.contact, name='blog-contact'),

    # Notifications
    path('notifications/', notifications, name='notifications'),

    # Post-related paths
    # Updated name to be more descriptive
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),

    # Home page (should be the last path if it's a general path)
    path('', PostListView.as_view(), name="blog-home"),
]
