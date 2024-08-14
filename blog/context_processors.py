# blog/context_processors.py
from .models import Post
from django.db.models import Count


def most_commented_posts(request):
    most_commented = Post.objects.annotate(
        comment_count=Count('comments')).order_by('-comment_count')[:5]
    return {'most_commented_posts': most_commented}
