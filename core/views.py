from time import sleep

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView

from core.forms import ImageForm
from core.language import correct_text
from core.models import Result
from core.text_recognition import extract_text


class LandingView(TemplateView):
    template_name = "core/landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class IndexView(FormView):
    template_name = "core/index.html"
    form_class = ImageForm

    def post(self, request, *args, **kwargs):
        raise SuspiciousOperation()


class ResultView(FormView):
    template_name = "core/result.html"
    form_class = ImageForm

    def get(self, request, *args, **kwargs):
        return redirect("core:index")

    def form_valid(self, form):
        image = form.cleaned_data["image"]

        result = Result()
        if self.request.user.is_authenticated:
            result.user = self.request.user
        result.image = image
        result.save()

        text = extract_text(result.image.path)
        corrected_text, correction_info = correct_text(text)

        result.text = text
        result.corrected_text = corrected_text
        result.correction_info = correction_info
        result.correct = result.text == result.corrected_text
        result.save()

        context_data = self.get_context_data(form=form)
        context_data["result"] = result

        return self.render_to_response(context=context_data)

    def form_invalid(self, form):
        return redirect("core:index")


class HistoryListView(LoginRequiredMixin, ListView):
    template_name = "core/history_list.html"
    model = Result
    context_object_name = "result_list"

    def get_queryset(self):
        return Result.objects.filter(user=self.request.user)[::-1]


class HistoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/history_detail.html"
    model = Result
    slug_url_kwarg = "slug"
    slug_field = "id"
    context_object_name = "result"
