from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from Fitness_store.fitness_app.forms import CustomUserCreationForm
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


class ProductPageView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfileRegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result
