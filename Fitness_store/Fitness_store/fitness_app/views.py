from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AboutUsPageView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SupplementsPageView(TemplateView):
    template_name = 'supplements.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GymEquipmentPageView(TemplateView):
    template_name = 'gym_equipment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
