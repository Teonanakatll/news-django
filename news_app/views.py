from django.shortcuts import render
from taggit.models import Tag
from django.db.models import Q

from . models import Category, Post
from . forms import SearchForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from . utils import get_page_obj, get_random_category
from haystack.query import SearchQuerySet

from django.views.decorators.cache import cache_page


# @cache_page(60 * 2)
def home(request):
    # print(request.GET.values())
    host = request.get_host()
    cats = Category.objects.filter(draft=False)

    # first_category = cats.get(slug='elektronika')
    first_category = cats[0]

    second_category = cats[1]

    third_category = cats[2]

    fourth_category = cats[3]

    random_cat_slug = cats[4]

    return render(request, 'news_app/home.html', locals())


# def paginator_mixin()


def category(request, cat_slug):

    template = 'news_app/category.html'
    cat = Category.objects.get(slug=cat_slug, draft=False)
    link_active = cat.id
    posts = cat.posts.filter(draft=False)

    first_cat = get_random_category(cat.id)

    second_cat = get_random_category((cat.id, first_cat.id))

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = get_page_obj(paginator, page_number)

    data = {
        'cat': cat,
        'page_obj': page_obj,
        'first_cat': first_cat,
        'second_cat': second_cat,
        'link_active': link_active
    }

    return render(request, template, context=data)



def about(request):
    # данные берём из context_processors
    link_active = 99

    return render(request, 'news_app/about.html', {'link_active': link_active})


def all_posts(request, tag_slug=None):
    posts = Post.objects.filter(draft=False).select_related('category')
    tag = None

    title = "Все статьи."

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
        title = f"Статьи по тегу - #{tag.name}"

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = get_page_obj(paginator, page_number)
    first_cat, second_cat = get_random_category()

    data = {
        'title': title,
        'page_obj': page_obj,
        'first_cat': first_cat,
        'second_cat': second_cat,
        'tag': tag,
    }

    return render(request, 'news_app/all-posts.html', context=data)


# @cache_page(60 * 2)
def post(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    host = request.get_host()
    random_cat = get_random_category()

    data = {
        'post': post,
        'host': host,
        'random_cat': random_cat[0],
    }

    return render(request, 'news_app/post.html', context=data)

def search_haystack(request):
    form = SearchForm()
    title = 'Страница поиска.'
    first_page_num = None
    first_cat, second_cat = get_random_category()
    search_list = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            # количество постов на странице поиска
            first_page_num = 10
            query = form.cleaned_data['query']
            query = f'"{query}"'
            title = f'результаты поиска по запросу - {query}.'

            posts_all = SearchQuerySet().autocomplete(content_auto=query)
            posts_all = [p for p in posts_all]
            count = len(posts_all)
            posts = posts_all[:first_page_num]


    data = {
        'form': form,
        'title': title,
        'query': query,
        'count': count,
        'first_page_num': first_page_num,
        'first_cat': first_cat,
        'second_cat': second_cat,
        'posts': posts,
        }

    return render(request, 'news_app/search.html', context=data)


def search_list(request, query, first_page_num):
    first_cat, second_cat = get_random_category()

    title = f'Статьи по запросу: {query}.'
    string = query
    query = query.replace('"', '')

    # posts = Post.objects.filter(id__in=lst).select_related('category')
    posts = SearchQuerySet().autocomplete(content_auto=query)
    posts = [p for p in posts]
    posts = posts[first_page_num:]

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = get_page_obj(paginator, page_number)

    data = {
        'page_obj': page_obj,
        'query': query,
        'title': title,
        'string': string,
        'first_cat': first_cat,
        'second_cat': second_cat,
    }

    return render(request, 'news_app/all-posts.html', context=data)


def tr_handler404(request, exception):

    return render(request=request, template_name='news_app/errors/error_page.html', status=404, context={
        'title': 'Страница не найдена: 404',
        'error_message': 'К сожалению такая страница не была найдена :(',
    })


def tr_handler500(request):

    return render(request=request, template_name='news_app/errors/error_page.html', status=500, context={
        'title': 'Ошибка сервера: 500',
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, отчет об ошибке мы направим администрации сайта',
    })


def tr_handler403(request, exception):

    return render(request=request, template_name='news_app/errors/error_page.html', status=403, context={
        'title': 'Ошибка доступа: 403',
        'error_message': 'Доступ к этой странице ограничен :(',
    })
