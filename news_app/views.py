from django.db.models import Count
from django.shortcuts import render
from taggit.models import Tag

from news import settings
from .models import Category, Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from random import randint

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

#
# class NewsCategory(ListView):
#     model = News

def category(request, cat_slug):

    template = 'news_app/category.html'
    cat = Category.objects.get(slug=cat_slug, draft=False)
    # cat = cats.get(slug=cat_slug)
    link_active = cat.id
    posts = cat.post_set.all()

    def get_random_category(num):
        while 1:
            rand = randint(1, num)
            if rand != cat.id:
                return Category.objects.filter(draft=False)[rand - 1]

    random_cat = get_random_category(Category.objects.filter(draft=False).count())

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    try:
        page_obj = paginator.get_page(page_number)
    # если указанная страница не является целым числом
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    # если указанный номер больше, чем всего страниц, возвращаем последнюю
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    data = {
        'cat': cat,
        'page_obj': page_obj,
        'random_cat': random_cat,
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

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    # если указанная страница не является целым числом
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    # если указанный номер больше, чем всего страниц, возвращаем последнюю
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    data = {
        'page_obj': page_obj,
        'tag': tag,
    }

    return render(request, 'news_app/all-posts.html', context=data)


# @cache_page(60 * 2)
def post(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    host = request.get_host()
    post_category = Category.objects.get(slug=category_slug)

    return render(request, 'news_app/post.html', {'post_category': post_category, 'post': post, 'host': host})

# def page_not_found_view(request, exception):
#     return render(request, f'{settings.ERRORS_TEMPLATES_PATH}/404.html', status=404)


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
        'error_message': 'Доступ к этой странице ограничен',
    })
