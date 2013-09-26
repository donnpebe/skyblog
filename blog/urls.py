from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    title = "SkyBlog"
    description = "Simple Blog for Superman"
    link = "/blog/feed/"

    def items(self):
        return Post.objects.all().order_by("-created")
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u"/blog/%d" % item.id

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(
                            queryset=Post.objects.all().order_by("-created")[:20],
                            template_name="blog/index.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
                            model=Post,
                            template_name="blog/detail.html")),
    url(r'^archives/$', ListView.as_view(
                            queryset=Post.objects.all().order_by("-created"), 
                            template_name="blog/archives.html")),
    url(r'^tag/(?P<tag>\w+-*\w+)$', 'tagged_post'),
    url(r'^feed/$', BlogFeed()),
)