from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DeleteView , CreateView
from django.urls import reverse_lazy

# posts = [
#     {
#         'author':'Destiny Franks',
#         'title':'Blog Post 1',
#         'content':'This is my first blog post',
#         'date_posted':'7th August, 2021'
        
#     },
#     {
#         'author':'Jane Doe',
#         'title':'Blog Post 2',
#         'content':'This is my second blog post',
#         'date_posted':'14th August, 2021'

#     }
# ]

# Create your views here.
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request,'blog/home.html',context) 


def about(request):
    return render(request,'blog/about.html',{'title':'About Page'}) 


class PostListView(ListView):
    model= Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

class PostDetailView(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html' 
    
class PostCreateView(CreateView):
    model = Post 
    fields = ['title', 'content']   
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog-home')