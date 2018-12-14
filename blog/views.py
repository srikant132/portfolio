from django.shortcuts import render
from .models import Blog                                         #to get blogs data import model 1
# Create your views here.
def allblogs(request):
    blogs = Blog.objects                                         #to get blog data from the database create object 2
    return render(request,'blog/allblogs.html',{'blogs':blogs})   #create a context here blogs 3
