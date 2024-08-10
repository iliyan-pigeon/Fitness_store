from django.test import TestCase, Client
from django.urls import reverse


class ContactsPageViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_contacts_page_view(self):
        response = self.client.get(reverse('contacts'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')
