# import datetime
from haystack import indexes
from . models import Post

#при ошибку с datetime_safe django5 его не поддерживает
#pip install git+https://github.com/django-haystack/django-haystack.git
# + необходимо установить setuptools

# rebuild_index

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    article = indexes.CharField(model_attr='article')
    time_create = indexes.DateTimeField(model_attr='time_create')
    content_auto = indexes.EdgeNgramField(model_attr='article')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(draft=False).select_related('category')
