from django.shortcuts import render, reverse
from .models import Post
from .forms import Post_form
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone




# Create your views here.
def home_page(request):
    post = Post.objects.values().order_by('-date')
    return render(request, 'home_page.html', {'post': post})

def post_view(request):
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        #    {'post_type': 'Boast', 'text': 'jkh'}
            print(data)
            boast = False
            roast = False
            if data['post_type'] == 'Boast':
                boast = True
            if data['post_type'] == 'Roast':
                roast = True
        #    print(Post.data.values())

            result = Post.objects.create(
                roast = roast,
                boast = boast,
                text = data['text'],
                up = 0,
                down = 0,
                date = timezone.datetime.now
            )

        #   redirecturl = request.POST.get('redirect', '/')
        #   return redirect(redirecturl)
            return HttpResponseRedirect(reverse('home'))
        else:
            print(post_form.errors)

    form = Post_form()
    return render(request, 'add_post.html', {'form': form})

def boast_view(request):
    boasts = Post.objects.filter(boast = 'True').order_by('-date')
    return render(request, 'boasts.html', {'boasts': boasts})

def roast_view(request):
    roasts = Post.objects.filter(roast = 'True').order_by('-date')
    return render(request, 'roasts.html', {'roasts': roasts})

def vote_up(request, element_id):
    vote = Post.objects.get(id=element_id)
    vote.up += 1
    vote.save()
    return HttpResponseRedirect(reverse('home'))

def vote_down(request, element_id):
    vote = Post.objects.get(id=element_id)
    vote.down += 1
    vote.save()
    return HttpResponseRedirect(reverse('home'))

def up_view(request):
    up = Post.objects.values().order_by('-up')
    return render(request, 'up.html', {'up': up})

def down_view(request):
    down = Post.objects.values().order_by('-down')
    return render(request, 'down.html', {'down': down})

