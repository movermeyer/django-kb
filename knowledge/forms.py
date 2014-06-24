from __future__ import unicode_literals

from haystack.forms import SearchForm

from .article.forms import ArticleForm
from .category.forms import CategoryForm


__all__ = [
    'ArticleForm',
    'CategoryForm',
    'SimpleSearchForm',
]


class SimpleSearchForm(SearchForm):
    pass