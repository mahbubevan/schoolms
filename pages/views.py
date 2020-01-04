from django.shortcuts import render,HttpResponse
from django.views import generic
# Create your views here.

def index(request):
    return render(request,'pages/index.html')

# class IndexView(generic.ListView):
#     template_name = 'pages/index.html'