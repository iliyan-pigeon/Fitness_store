from django.test import TestCase
from django.contrib.auth import get_user_model
from Fitness_store.fitness_app.forms import CustomSetPasswordForm

UserModel = get_user_model()


class CustomSetPasswordFormTest(TestCase):

    def test_valid_set_password(self):
        user = UserModel.objects.create_user(username='testuser', password='testpassword123')
        form_data = {
            'new_password1': 'newtestpassword123',
            'new_password2': 'newtestpassword123'
        }
        form = CustomSetPasswordForm(user=user, data=form_data)

        self.assertTrue(form.is_valid())

