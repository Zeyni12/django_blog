from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DeleteView , CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


class PostListView(LoginRequiredMixin, ListView):
    model= Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

class PostDetailView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_detail.html' 
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content' ]
    
    def form_valid(self, form):
        form.instance.author =  self.request.user 
        return super().form_valid(form)
    
        
    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog-home')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content' ]
    
    def form_valid(self, form):
        form.instance.author =  self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False