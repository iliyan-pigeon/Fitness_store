from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

from Fitness_store.fitness_app.models import FitnessUser, Order

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
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'profile_picture']
        #labels = {
        #    'first_name': 'First Name:',
        #    'last_name': 'Last Name:',
        #    'image_url': 'Image URL:',
        #    'age': 'Age:',
        #}


class CustomPasswordChangeForm(auth_forms.PasswordChangeForm):
    pass


class CustomPasswordResetForm(PasswordResetForm):
    pass


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label='')


#class ShippingAddressForm(forms.ModelForm):
#
#    class Meta:
#        model = ShippingAddress
#        fields = ['address', 'city', 'region', 'zipcode']
