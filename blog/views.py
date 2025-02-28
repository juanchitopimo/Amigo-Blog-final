from django.shortcuts import render, redirect
from .models import Post, Comment, Notification
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
import logging
from users.views import notifications
from django.contrib.messages.views import SuccessMessageMixin


# Set up logging
logger = logging.getLogger(__name__)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = self.request.user
            new_comment.save()
            return redirect('post-detail', pk=post.pk)
        else:
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_message = "post  was created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        return response


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_message = "post  was updated successfully"

    def form_valid(self, form):
        response = super().form_valid(form)

        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    success_message = "post was deleted successfully"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact Us'})


def notifications(request):
    notifications = Notification.objects.filter(user=request.user, read=False)
    logger.info(f'Found {notifications.count()} unread notifications for user {
                request.user.username}')
    notifications.update(read=True)
    context = {
        'notifications': notifications
    }
    return render(request, 'blog/notifications.html', context)
