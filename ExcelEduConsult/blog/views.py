from .models import Post, Tag
from django.shortcuts import render

# Create your views here.
def index(request):
    latest_post = Post.objects.last()
    posts = Post.objects.order_by('-date_posted')[:10]
    context = {
        'latest_post': latest_post,
        'posts': posts
    }
    return render(request, 'index.html', context)


def detail(request, slug):                           # get the id of the post from the url
    post = Post.objects.get(slug=slug)            # get the post that you want to show its comments using the id gotten from the url
    context = {                                               # this is everything we want to show in our post html template. (Everyting we've gotten above)
        'post': post,
    }
    return render(request, 'article.html', context)

def tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    posts = tag.post_set.order_by('-date_updated')
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/tag.html', context)