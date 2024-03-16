from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .views import home, category, about, all_posts, post, cloud

from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from .sitemap import PostSitemap, CategorySitemap, StaticSitemap

sitemaps = {
    'posts': PostSitemap,
    'category': CategorySitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    path('', home, name='home'),
    # path('', cache_page(60 * 60)(WomenHome.as_view()), name='home'),
    path('blog/<slug:cat_slug>/', category, name='category'),
    path('about/', about, name='about'),
    path('all-posts/', all_posts, name='all_posts'),
    path('tag/<slug:tag_slug>/', all_posts, name='all_posts_by_tag'),
    path('<slug:category_slug>/<slug:post_slug>/', post, name='post'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='news_app/robots.txt',
         content_type='text/plain')),

    path('cloud/', cloud, name='cloud'),


]
