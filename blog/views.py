from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post

#Function-based view:
def home(request):
    Context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', Context)


# Class-based view: displaying posts using list of posts objects.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' # variable used to iterate in the listview to render the html document
    ordering = ['-date_posted'] # is used for ordering of posts objects in the listview, recently updated post will come at the most top of the listview
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' # variable used to iterate in the listview to render the html document
    paginate_by = 3

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get['username'])
        return Post.objects.filter(author=user).order_by('-date_posted')

# Class-based view: displaying individual post details through DetailView  by specifying the post object ID
class PostDetailView(DetailView):
    model = Post


# Class-based view: displaying individual post details through DetailView  by specifying the post object ID
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # setting author of the post to current user before creating the post
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # setting author of the post to current user before creating the post
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = 'blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
