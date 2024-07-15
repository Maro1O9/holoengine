from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .forms import PostForm, MediaForm
from .models import Post, Media

# Create your views here.


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            media_types = request.POST.getlist('media_type')
            files = request.FILES.getlist('file')
            for media_type, file in zip(media_types, files):
                Media.objects.create(post=post, media_type=media_type, file=file)
            return redirect('post_detail', post_id=post.id)
    else:
        post_form = PostForm()
        media_form = MediaForm()
    return render(request, "create_post.html", {'post_form': post_form, 'media_form': media_form})
      

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

