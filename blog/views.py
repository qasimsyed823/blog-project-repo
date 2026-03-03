from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.views.generic import DeleteView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,'blog/post_detail.html',{'post':post})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #fields = ['title', 'content', 'published']
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}! You can now login.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {"form": form})


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = Post
    fields = ['title', 'content', 'published']
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



