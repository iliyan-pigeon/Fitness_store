from django.contrib.auth import login, get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views
from Fitness_store.fitness_app.forms import LoginForm, RegisterUserForm, ProfileEditForm, CustomPasswordChangeForm, \
    CustomPasswordResetForm
from Fitness_store.fitness_app.models import Supplements, GymEquipment, Cart, CartItem, FitnessUser
from Fitness_store.fitness_app.utils import get_or_create_cart

UserModel = get_user_model()


class HomePageView(views.TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_selling_supplements'] = Supplements.objects.filter(best_selling=True)
        context['best_selling_gym_equipment'] = GymEquipment.objects.filter(best_selling=True)
        return context


class AboutUsPageView(views.TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SupplementsPageView(views.ListView):
    model = Supplements
    template_name = 'supplements.html'


class GymEquipmentPageView(views.ListView):
    model = GymEquipment
    template_name = 'gym_equipment.html'


class ContactsPageView(views.TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EquipmentProductPageView(views.DetailView):
    model = GymEquipment
    template_name = 'equipment_product.html'


class SupplementProductPageView(views.DetailView):
    model = Supplements
    template_name = 'supplement_product.html'


class RegisterUserView(views.CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm


@method_decorator(login_required, name='dispatch')
class LogoutUserView(auth_views.LogoutView):
    pass


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(views.DetailView):
    model = FitnessUser
    template_name = 'profile_details.html'

    def get_context_data(self, **kwargs):
        profile_picture = static('images/istockphoto-1433039224-1024x1024.jpg')

        if self.object.profile_picture is not None:
            profile_picture = self.object.profile_picture

        context = super().get_context_data(**kwargs)
        context[profile_picture] = profile_picture

        return context


@method_decorator(login_required, name='dispatch')
class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ProfileDeleteView(views.DeleteView):
    model = FitnessUser
    template_name = 'profile_delete.html'  # Replace with the template name you prefer
    success_url = reverse_lazy('logout')  # Redirect to the logout view after deletion

    def get_object(self, queryset=None):
        return self.request.user


def add_to_cart(request, product_type, product_id):
    product = None
    if product_type == 'supplement':
        product = get_object_or_404(Supplements, id=product_id)
    elif product_type == 'gym_equipment':
        product = get_object_or_404(GymEquipment, id=product_id)

    if product:
        cart = get_or_create_cart(request)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            name=product.name,
            price=product.price,
            defaults={'quantity': 1},
            product_id=product.id,
            product_type=product_type
        )
        if cart_item.quantity < product.amount_in_stock:
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        elif cart_item.quantity >= product.amount_in_stock:
            error_message = "Item quantity exceeds available stock."
            return HttpResponseBadRequest(render(request, 'out_of_stock.html', {'error_message': error_message}))

    return redirect('homepage')


def remove_from_cart(request, product_type, product_id):
    product = None
    if product_type == 'supplement':
        product = get_object_or_404(Supplements, id=product_id)
    elif product_type == 'gym_equipment':
        product = get_object_or_404(GymEquipment, id=product_id)

    if product:
        cart = get_or_create_cart(request)

        cart_item = CartItem.objects.filter(cart=cart, name=product.name).first()
        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

    return redirect('homepage')


@method_decorator(login_required, name='dispatch')
class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('password change done')


@method_decorator(login_required, name='dispatch')
class PasswordChangeDoneView(views.TemplateView):
    template_name = 'password_change_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password reset done')


def complete_order(request):
    cart = None
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
    else:
        cart = Cart.objects.get(id=request.session['cart_id'])

    for i in CartItem.objects.filter(cart_id=cart.id):
        product = None
        if i.product_type == "supplement":
            product = Supplements.objects.get(id=i.product_id)
        elif i.product_type == "gym_equipment":
            product = GymEquipment.objects.get(id=i.product_id)

        product.amount_in_stock -= i.quantity
        product.save()

    return redirect('homepage')
