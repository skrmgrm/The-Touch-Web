from django.shortcuts import get_object_or_404, render
from .models import PublishedManger, Post
from taggit.models import Tag
from django.db.models import Count
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

# Create your views here.


def home(request, tag_slug=None):
    # object_list = Post.published.all()
    object_list = Post.published.all().exclude()[1:12]
    object_list2 = Post.published.all().exclude()[12:]

    # tags
    # tag = None

    # if tag_slug:
    #     tag = get_object_or_404(Tag, slug=tag_slug)
    #     object_list = object_list.filter(tags__in=[tag])
    try:
        latest_post = Post.published.latest('id')
    except Post.DoesNotExist:
        latest_post = None

    context = {
        'object': object_list,
        'object2': object_list2,
        'latest_post': latest_post
    }

    return render(request, 'touch/home.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)

    # list of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(
        tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count(
        'tags')).order_by('-same_tags', '-publish')[:4]

    context = {
        'post': post,
        'similar_posts': similar_posts,
    }

    return render(request, 'touch/detail.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    object_list = Post.published.filter(tags=tag)
    context = {
        'tag': tag,
        'common_tags': common_tags,
        'object': object_list,
    }
    return render(request, 'touch/tags.html', context)


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'body', 'tags']
#     success_url = '/'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.save()
#         return super(PostCreateView, self).form_valid(form)

def about(request):
    return render(request, 'touch/about.html')


def contact(request):
    return render(request, 'touch/contact.html')
