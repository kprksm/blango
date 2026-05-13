from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView,DetailView,TemplateView, View
from blog.models import Post,Comment,Tag
from django.utils import timezone
from blog.forms import CommentForm

# Create your views here.

class indexView(View):
  def get(self,request):
    posts = Post.objects.all()
    return render(request,"blog/index.html", {"posts" : posts})


def post_detail(request, slug):
    post = get_object_or_404(Post,slug = slug)

    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(request,"blog/post_detail.html", {"post" : post, "comment_form" : comment_form})
