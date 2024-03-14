from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post, Category, About


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Category.objects.filter(draft=False)


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Post.objects.filter(draft=False)

    def lastmod(self, obj):
        return obj.time_update


class StaticSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.7

    def items(self):
        return ['home', 'all_posts', 'about']

    def location(self, item):
        return reverse(item)
