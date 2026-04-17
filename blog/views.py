from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView, View


# Create your views here.

class indexView(View):
  def get(self,request):
    return render(request,"blog/index.html")

