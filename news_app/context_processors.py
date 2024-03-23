from django.shortcuts import get_object_or_404

from .models import Category, About


def get_category(request):
    category = Category.objects.prefetch_related('posts').filter(draft=False)
    about = get_object_or_404(About, pk=1)

    return locals()
