from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView, View
from blog.models import Post,Comment,Tag
from django.utils import timezone

# Create your views here.

class indexView(View):
  def get(self,request):
    posts = Post.objects.all()
    return render(request,"blog/index.html", {"posts" : posts})


def post_detail(request, slug):
  post = get_object_or_404(Post,slug = slug)
  return render(request,"blog/post_detail.html", {"post" : post})
