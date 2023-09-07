from django.contrib.auth import login, get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from Fitness_store.fitness_app.forms import LoginForm, RegisterUserForm
from Fitness_store.fitness_app.models import Supplements, GymEquipment


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailView(views.DetailView):
    model = UserModel
    template_name = 'profile_details.html'

    def get_context_data(self, **kwargs):
        profile_picture = static('images/istockphoto-1433039224-1024x1024.jpg')

        if self.object.profile_picture is not None:
            profile_picture = self.object.profile_picture

        context = super().get_context_data(**kwargs)
        context[profile_picture] = profile_picture

        return context


class ProfileEditView(views.UpdateView):
    pass


class ProfileDeleteView(views.DeleteView):
    pass
