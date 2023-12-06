from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth import get_user_model
from Fitness_store.fitness_app.forms import ProfileEditForm

UserModel = get_user_model()


class ProfileEditFormTest(TestCase):

    def test_valid_profile_edit(self):
        user = UserModel.objects.create_user(username='testuser', password='testpassword123')
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
        form = ProfileEditForm(instance=user, data=form_data)
        self.assertTrue(form.is_valid())
        