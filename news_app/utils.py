from django.core.paginator import PageNotAnInteger, EmptyPage

from random import randint

from . models import Category


def get_page_obj(paginator, page_number):
    try:
        page_obj = paginator.get_page(page_number)
    # если указанная страница не является целым числом
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    # если указанный номер больше, чем всего страниц, возвращаем последнюю
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj


def get_random_category(cat=None):
    #  если передаём кортеж
    if type(cat) is tuple:
        category = Category.objects.filter(draft=False).exclude(id__in=cat)
        num = category.count()
        rand = randint(1, num)
        return category[rand - 1]

    category = Category.objects.filter(draft=False)
    num = category.count()
    # если передаём id
    if cat:
        while 1:
            rand = randint(1, num)
            if rand != cat:
                return category[rand - 1]

    rand = randint(1, num)
    first_cat = category[rand - 1]
    if first_cat.id > 1:

        second_cat = category[first_cat.id - 2]
    else:
        second_cat = category[first_cat.id + 1]
    return first_cat, second_cat
