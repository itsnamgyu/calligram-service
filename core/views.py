from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView


class LandingView(TemplateView):
    template_name = "core/landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexView(TemplateView):
    template_name = "core/index.html"


class ResultView(TemplateView):
    template_name = "core/result.html"

