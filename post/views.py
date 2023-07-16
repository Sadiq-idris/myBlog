from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from .models import Post, Comment
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class Posts(LoginRequiredMixin, generic.CreateView):
    model = Post
    exra_context = {
        "title":"New Post",
    }
    fields = ["thumbnail", "title", "content","conclusion", "tag"]
    template_name = "post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailPost(generic.DetailView):
    model = Post
    exra_context = {
        "title":"Detail Post",
    }
    template_name = "detail_post.html"
    context_object_name = "post"


class UpdatePost(LoginRequiredMixin, generic.UpdateView):
    model = Post
    exra_context = {
        "title":"Detail Post",
    }
    fields = ["thumbnail", "title", "content", "conclusion"]
    template_name = "update_post.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:

            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = Post
    exra_context = {
        "title":"Confirm",
    }

    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:

            raise PermissionDenied
    
        return super().dispatch(request, *args, **kwargs)


def sendComment(request):
    comment = request.POST["comment"]
    # username = request.POST["username"]
    post_id = request.POST["post_id"]

    post = Post.objects.get(id=post_id)

    comment = Comment(comment_username=request.user, post=post, comment=comment)
    comment.save()

    return HttpResponse("message sent successfull")


def getComment(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)

  
    return JsonResponse({"comments":list(comments.values())})