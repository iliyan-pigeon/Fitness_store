from django.core.exceptions import ValidationError
from django.test import TestCase
from Fitness_store.fitness_app.forms import ProductSearchForm


class ProductSearchFormTest(TestCase):
    SEARCH_QUERY_MAX_LENGTH = 100

    def test_valid_search_query(self):
        form_data = {'search_query': 'test query'}
        form = ProductSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


