from django.shortcuts import render
from post.models import Post
from django.core.paginator import Paginator


def home(request):
    title = "Home"
    posts = Post.objects.all()
    paginator = Paginator(posts,6)
    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "index.html", {"title":title,"page_obj":page_obj})

def about_us(request):
    title = "About-Us"

    return render(request, "about_us.html", {"title":title})