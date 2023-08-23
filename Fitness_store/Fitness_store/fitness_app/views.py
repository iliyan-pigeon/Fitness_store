from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, FormView, DetailView

from Fitness_store.fitness_app.forms import LoginForm, RegisterUserForm
from Fitness_store.fitness_app.models import BestSellingSupplements, BestSellingGymEquipment, Supplements, GymEquipment


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_selling_supplements'] = BestSellingSupplements.objects.all()
        context['best_selling_gym_equipment'] = BestSellingGymEquipment.objects.all()
        return context


class AboutUsPageView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SupplementsPageView(ListView):
    model = Supplements
    template_name = 'supplements.html'


class GymEquipmentPageView(ListView):
    model = GymEquipment
    template_name = 'gym_equipment.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EquipmentProductPageView(DetailView):
    model = GymEquipment
    template_name = 'equipment_product.html'


class SupplementProductPageView(DetailView):
    model = Supplements
    template_name = 'supplement_product.html'


class RegisterUserView(CreateView):
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class ProfileLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('homepage')
