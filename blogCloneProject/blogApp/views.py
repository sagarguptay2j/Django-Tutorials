from django.shortcuts import render,get_object_or_404,redirect_field_name
frm django.utils import timezone
from blogApp.models import Post,Comment
from blogApp.forms import CommentForm,PostForm
from django.contrib.auth.decorators import login_recquired
from django.contrib.auth.mixins import LoginRecquiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views .
class AboutView(TemplateView):
    template_name = 'blogApp/about.html'

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRecquiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRecquiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    form_class = PostForm
    model = Post

class DeletePostView(LoginRecquiredMixin,DeleteView):
    login_url = '/login/'
    success_url = 'blogApp/post_list.html'
    model = Post

class DraftListView(LoginRecquiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blogApp/post_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('-created_date')



@login_recquired
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish
    return redirect('post_detail',pk=pk)


@login_recquired
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(comment = False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=pk)
        else:
            form = CommentForm()
        return render(request,'blogApp/comment_form.html',{'form':form})

@login_recquired
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_recquired
def comment_delete(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
