from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')[:10]
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
        comment_text = request.POST.get('comment')
        Comment.objects.create(post=post, user=request.user, text=comment_text)
        return HttpResponseRedirect(reverse('post_detail', args=[pk]))
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        tags = request.POST.get('tags')
        Post.objects.create(title=title, content=content, image=image, category=category, tags=tags, author=request.user)
        return HttpResponseRedirect('/')
    return render(request, 'blog/create_post.html')



def custom_404(request, exception):
    return render(request, 'blog/404.html', status=404)
