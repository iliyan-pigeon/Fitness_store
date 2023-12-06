from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from Fitness_store.fitness_app.forms import RegisterUserForm


class RegisterUserFormTest(TestCase):

    def test_valid_registration(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'gender': 'M',
            'profile_picture': SimpleUploadedFile('test_photo.jpg', b'content', content_type='image/jpeg')
        }
        form = RegisterUserForm(data=form_data)

        self.assertTrue(form.is_valid())
