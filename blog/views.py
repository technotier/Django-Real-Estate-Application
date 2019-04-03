from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):

    blog = Article.objects.order_by('-posted_on')

    paginator = Paginator(blog, 6)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)

    context = {
        "blog": paged_blog
    }

    return render(request, "blog/post.html", context)

def single_blog(request, blog_id):

    single_blog = get_object_or_404(Article, id=blog_id)

    context = {
        "single_blog": single_blog
    }

    return render(request, "blog/single.html", context)