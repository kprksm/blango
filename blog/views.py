from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView, View
from blog.models import Post,Comment,Tag
from django.utils import timezone

# Create your views here.

class indexView(View):
  def get(self,request):
    posts = Post.objects.all()
    return render(request,"blog/index.html", {"posts" : posts})

