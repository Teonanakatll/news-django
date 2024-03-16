from django.db import models
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager
from unidecode import unidecode


class Category(models.Model):
    """Категории статей"""

    # добавить дату редактирования
    name = models.CharField("Название", max_length=30, db_index=True)
    description = models.CharField("Описание", max_length=255, blank=True)
    slug = models.SlugField("url", max_length=255, unique=True, db_index=True)
    image = models.ImageField("Фото", upload_to="category_img/", blank=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]


class About(models.Model):
    """О сайте"""
    name = models.CharField("Название", max_length=70, blank=True)
    header = models.CharField("Заголовок", max_length=70)
    header_article = models.CharField("Заголовок статьи", max_length=70)
    article = CKEditor5Field("Текст статьи", config_name='extends')
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "О сайте"


class Post(models.Model):
    """Статья"""
    #
    header = models.CharField("Заголовок", max_length=350)
    short = models.CharField("Короткий заголовок", max_length=150, blank=True)

    article = CKEditor5Field("Статья", config_name='extends')
    time_create = models.DateTimeField("Дата добавления", auto_now_add=True)
    time_update = models.DateTimeField("Дата редактирования", auto_now=True)
    image = models.ImageField("Фото", upload_to="news_img/%Y/%h/%d", blank=True)
    slug = models.SlugField("url", unique=True, db_index=True)
    draft = models.BooleanField("Черновик", default=False)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()

    def get_category_slug(self):
        category_slug = self.category.slug
        return category_slug

    def __str__(self):
        return self.short

    def get_absolute_url(self):
        return reverse('post', kwargs={'category_slug': self.get_category_slug(), 'post_slug': self.slug})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["id"]


class PostPhoto(models.Model):
    """Фото к статье"""
    name = models.CharField("Название", max_length=350, blank=True)
    photo = models.ImageField("Фото", upload_to="news_img/%Y/%h/%d")
    date = models.DateTimeField("Добавлено", auto_now_add=True)
    post = models.ForeignKey(Post, verbose_name="Статья", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фото статей"
        verbose_name_plural = "Фото статей"
        ordering = ['date']
