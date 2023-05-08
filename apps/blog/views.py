from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count


def post_list(request, tag_slug=None):
    posts = Post.published.all()
    common_tags = Post.tags.most_common()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag, slug=tag_slug)
        posts=posts.filter(tags__in=[tag])
        
        paginator = Paginator(posts, 3)
        
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        
        context={
            'posts' : posts,
            'page' : page,
            'tag' : tag,
            'common_tags' : common_tags
        }
        
        return render(request, 'blog_list.html', context)