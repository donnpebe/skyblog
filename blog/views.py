from .models import Post
from django.shortcuts import render_to_response

def tagged_post(request, tag):
    posts = Post.objects.filter(tags__slug=tag)
    return render_to_response("blog/tagged_post.html", {"posts":posts, "tag":tag})