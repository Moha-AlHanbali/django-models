from django.db import models
from django.views.generic import ListView, DeleteView, TemplateView
from .models import Snack


class HomeView(TemplateView):
    template_name = "home.html"


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack


class SnackDetailView(DeleteView):
    template_name = "snack_detail.html"
    model = Snack
    context_object_name = 'snack_object'