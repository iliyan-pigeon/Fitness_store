from django.test import TestCase
from django.contrib.auth import get_user_model
from Fitness_store.fitness_app.forms import LoginForm

UserModel = get_user_model()


class LoginFormTest(TestCase):

    def test_valid_login(self):
        user = UserModel.objects.create_user(username='testuser', password='testpassword123')
        form_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        