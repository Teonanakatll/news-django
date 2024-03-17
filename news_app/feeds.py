from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    #TODO: сделать модель с донными сайта
    #TODO: прописать метатеги для всех страниц
    title = 'Geektop.ru'
    link = '/'
    description = 'Новые статьи на сайте Geektop.ru.'

    def items(self):
        return Post.objects.all()[:5]

    def item_title(self, item):
        return item.short

    def item_description(self, item):
        return truncatewords(item.header, 30)