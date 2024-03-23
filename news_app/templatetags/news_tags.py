from django import template
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404

# taggit
from collections import defaultdict, Counter

from news_app.models import *

register = template.Library()


@register.inclusion_tag('news_app/tags/menu.html')
def show_menu(menu, about, link_active=0):

    return locals()


@register.inclusion_tag('news_app/tags/widgets/wid-last-category-articles.html')
def get_last_category_articles(cats):

    lst = []
    for cat in cats:
        lst.append(cat.posts.filter(draft=False).first())

    return locals()


@register.inclusion_tag('news_app/tags/widgets/wid-read-more.html')
def read_more(post):
    links = Post.objects.filter(category__name=post.category.name, draft=False).exclude(id=post.id)[:5].select_related('category')
    category = post.category

    return locals()


@register.inclusion_tag('news_app/tags/widgets/wid-settings-tags-cloud.html')
def get_tags_cloud_script():
    # просто возвращает список отсортированный убыванию количества
    tags = Post.tags.most_common()[:30]

    return locals()


@register.inclusion_tag('news_app/tags/home/items-first-section.html')
def get_items_first_section(category, host):
    lst = Post.objects.filter(category__slug=category.slug, draft=False)[:5].select_related('category')

    if len(lst) == 5:
        col_6 = lst[3:]
        col_4 = lst[:3]
    else:
        message = f"Для вывода блока требуется 5 статей в категории '{category.slug}'"

    host = host

    return locals()


@register.inclusion_tag('news_app/tags/home/items-second-section.html')
def get_items_second_section(cat):
    # lst = category.post_set.filter(draft=False).reverse()[:4].select_related('category')
    lst = Post.objects.filter(category__slug=cat.slug, draft=False)[:4].select_related('category')
    if len(lst) > 1:
        col_4 = lst
    else:
        message = f"Для вывода блока требуется минимум 2 статьи в категории '{cat.slug}'"

    category = cat

    return locals()


@register.inclusion_tag('news_app/tags/home/items-third-section.html')
def get_items_third_section(cat):
    lst = cat.posts.filter(draft=False)[:4]

    if len(lst) > 1:
        col_3 = lst
    else:
        message = f"Для вывода блока требуется минимум 2 статьи в категории '{cat.slug}'"

    category = cat

    return locals()


@register.inclusion_tag('news_app/tags/home/items-fourth-section.html')
def get_items_fourth_section(category):
    lst = category.posts.filter(draft=False)[:4].select_related('category')
    category = category

    if len(lst) > 1:
        col_6 = lst
    else:
        message = f"Для вывода блока требуется минимум 2 статьи в категории '{category.slug}'"

    return locals()


@register.inclusion_tag('news_app/tags/type-one-section.html')
def get_type_one_section(random_cat):

    lst = random_cat.posts.filter(draft=False)[:3].select_related('category')
    category = random_cat

    if len(lst) > 2:
        big = lst[0]

        small = lst[1:]
    else:
        message = f"Для вывода блока требуется минимум 2 статьи в категории '{random_cat.slug}'"

    return locals()

