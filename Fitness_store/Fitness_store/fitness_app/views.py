from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic as views
from Fitness_store.fitness_app.forms import LoginForm, RegisterUserForm, ProfileEditForm, CustomPasswordChangeForm, \
    ProductSearchForm, OrderAddressForm
from Fitness_store.fitness_app.models import Supplements, GymEquipment, Cart, CartItem, FitnessUser, Order, OrderItem
from Fitness_store.fitness_app.utils import get_or_create_cart, get_or_create_order
from decouple import config

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
        form.instance.user = self.request.user
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
    template_name = 'profile_delete.html'
    success_url = reverse_lazy('homepage')

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


def complete_order(request):
    if request.method == 'POST':
        form = OrderAddressForm(request.POST)
        if form.is_valid():
            shipping_details = form.save(commit=False)
            cart = None
            order = get_or_create_order(request)
            if request.user.is_authenticated:
                cart = Cart.objects.get(user=request.user)
                shipping_details.user = request.user
                order.user = shipping_details.user
            else:
                cart = get_or_create_cart(request)
                shipping_details.session_key = request.session.session_key
                cart.session_key = shipping_details.session_key
                cart.save()
                order.session_key = shipping_details.session_key

            order.address = shipping_details.address
            order.city = shipping_details.city
            order.region = shipping_details.region
            order.zipcode = shipping_details.zipcode
            order.date_added = shipping_details.date_added
            order.save()

            for i in CartItem.objects.filter(cart_id=cart.id):
                product = None
                if i.product_type == "supplement":
                    product = Supplements.objects.get(id=i.product_id)
                elif i.product_type == "gym_equipment":
                    product = GymEquipment.objects.get(id=i.product_id)

                product.amount_in_stock -= i.quantity
                product.save()

                order_item, created = OrderItem.objects.get_or_create(
                    order=order,
                    name=product.name,
                    price=product.price,
                    quantity=i.quantity,
                    product_id=product.id,
                    product_type=i.product_type,
                )
                order_item.save()
                i.delete()

            return redirect('homepage')

    else:
        form = OrderAddressForm()
        cart = get_or_create_cart(request)
        cart.session_key = request.session.session_key
        cart.save()

    return render(request, 'complete_order.html', {'form': form})


def search_product(request):
    form = ProductSearchForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        supplements = Supplements.objects.filter(name__icontains=search_query)
        gym_equipment = GymEquipment.objects.filter(name__icontains=search_query)
        return render(request, 'search_results.html', {'supplements': supplements, 'gym_equipment': gym_equipment})


def orders_for_delivery(request):
    orders = Order.objects.all()

    return render(request, 'orders_for_delivery.html', {'orders': orders})


def order_details(request, pk):
    order = Order.objects.get(pk=pk)

    return render(request, 'order_details.html', {'order': order})


@staff_member_required
def clear_session(request):
    request.session.flush()
    return redirect('homepage')
