from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views import View
from .models import Post
from .forms import PostForm


# Create your views here.


def viewNewsFeed(request):

    context = {
    }

    return render(request, 'newsFeed/newsFeed.html', context)



class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        val = False


        context = {
            'post_list': posts,
            'form': form,
        }

        print(posts)

        return render(request, 'newsFeed/newsFeed.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form = PostForm(request.POST)
        val = False


        context = {
            'post_list': posts,
            'form': form,
        }

        print(posts)

        return render(request, 'newsFeed/newsFeed.html', context)
