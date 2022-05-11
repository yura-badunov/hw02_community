from django.shortcuts import get_object_or_404, render
from .models import Group, Post
from django.conf import settings


def index(request):
    posts = Post.objects.all()[:settings.POSTS_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.POSTS_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
