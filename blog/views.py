from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    post = Post.objects.filter(pubished_date__lte=timezone.now()).order_by('pubished_date')
    return render(request,'blog/post_list.html',{'posts':post})
