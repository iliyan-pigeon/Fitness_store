from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.models import User

from Fitness_store.fitness_app.models import FitnessUser

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):

    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'gender', 'profile_picture']


class LoginForm(auth_forms.AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'gender', 'profile_picture']
        #labels = {
        #    'first_name': 'First Name:',
        #    'last_name': 'Last Name:',
        #    'image_url': 'Image URL:',
        #    'age': 'Age:',
        #}
