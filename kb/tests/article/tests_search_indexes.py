from __future__ import unicode_literals

from django.core.management import call_command
from model_mommy import mommy

from kb.tests.test import SearchViewTestCase
from kb.models import Article
from kb.views import SearchView


class SearchArticleTestCase(SearchViewTestCase):

    view_function = SearchView
    view_name = 'search'

    def setUp(self):
        mommy.make_recipe('kb.tests.category_with_articles')

        for article in Article.objects.all():
            article.tags.add('bar')

        call_command('rebuild_index', interactive=False, verbosity=0)

    def test_search_title(self):
        response = self.get({'q': 'published article title'})
        object_list = response.context['page'].object_list

        self.assertHttpOK(response)
        self.assertSeqEqual([a.object for a in object_list], Article.objects.published())

    def test_search_content(self):
        response = self.get({'q': 'published article content'})
        object_list = response.context['page'].object_list

        self.assertHttpOK(response)
        self.assertSeqEqual([a.object for a in object_list], Article.objects.published())

    def test_search_tag(self):
        response = self.get({'q': 'bar'})
        object_list = response.context['page'].object_list

        self.assertHttpOK(response)
        self.assertSeqEqual([a.object for a in object_list], Article.objects.published())

    def test_search_draf_article_should_fail(self):
        response = self.get({'q': 'draft article title'})
        object_list = response.context['page'].object_list

        self.assertHttpOK(response)
        self.assertFalse([a.object for a in object_list])
