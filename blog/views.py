# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Post



def post_list(request):
    posts = Post.objects.filter(title='Life')
    return render(request, 'blog/post_list.html', {'posts': posts})
