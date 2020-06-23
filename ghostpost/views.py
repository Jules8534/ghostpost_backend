from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost.models import Post, Sorter
from ghostpost.forms import Post_form
from datetime import datetime as dt
# from django.utils.timezone import timezone 
from ghostpost.helpers import private_url_maker



# Create your views here.
def index(request):
    html = "index.html"
    post_form = Post_form()
    posts = Post.objects.all()
    post_type = request.GET.get('type')
    if post_type == 'boast':
        posts = posts.filter(boast=True)
    elif post_type == 'roast':
        posts = posts.filter(boast=False)
    sort = request.GET.get('sort')
    if sort == 'up':
        posts = posts.order_by('-score')
    elif sort == 'down':
        posts = posts.order_by('score')

    if request.method == "POST":
        form = Post_form(request.POST)
        if form.is_valid():
            boast = form.cleaned_data.get("boast")
            text = form.cleaned_data.get("text")
            Post.objects.create(
                boast=boast,
                text=text,
                up=0,
                down=0,
            )
    return render(request, html, {
        "current_path": request.path, "post_form": post_form, "ghostpost": posts
    })




def ghost_public_detail(request, pk):
    html =  "ghost_detail.html"
    ghost = Post.objects.get(pk=pk)
    private = False
    return render(request, html, {"ghost": ghost, "private": private})

def ghost_private_detail(request, private_url):
    html = "ghost_detail.html"
    ghost = Post.objects.get(pk=pk)
    private = False
    return render(request, html, {"ghost": ghost, "private": private})


def vote_up(request, pk):
    post = Post.objects.get(id=pk)
    post.up += 1
    post.save()
    return HttpResponseRedirect(reverse("home"))

def vote_down(request, pk):
    post = Post.objects.get(id=pk)
    post.down += 1
    post.save()
    return HttpResponseRedirect(reverse("home"))

def up_view(request, pk):
    post = Post.objects.get(id=pk)
    post.up_view += 1
    post.save()
    return HttpResponseRedirect(reverse("home"))

def down_view(request, pk):
    post = Post.objects.get(id=pk)
    post.down_view += 1
    post.save()
    return HttpResponseRedirect(reverse("home"))

def delete_post(request, private_url):
    deleted = Post.objects.get(private_url=private_url).delete()
    return HttpResponseRedirect(reverse("home"))

