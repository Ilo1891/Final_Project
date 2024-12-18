from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from reservation.forms import (ReservationForm, ReservationUpdateForm,
                               TableForms)
from reservation.models import Reservation, Table
from reservation.users_cases import save_feedback


class TableTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "reservation/home.html"


class TableCreateView(LoginRequiredMixin, CreateView):
    model = Table
    form_class = TableForms
    success_url = reverse_lazy("reservation:table_list")

    def form_valid(self, form):
        message = form.save()
        message.owner = self.request.user
        message.save()
        return super().form_valid(form)


class TableListView(LoginRequiredMixin, ListView):
    model = Table


class TableDetailView(LoginRequiredMixin, DetailView):
    model = Table


class TableUpdateView(LoginRequiredMixin, UpdateView):
    model = Table
    form_class = TableForms
    success_url = reverse_lazy("reservation:table_list")


class TableDeleteView(LoginRequiredMixin, DeleteView):
    model = Table
    success_url = reverse_lazy("reservation:table_list")


class ReservationListView(ListView):
    model = Reservation
    title = "Бронирование"


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = "reservation/reservation.html"
    form_class = ReservationForm
    success_url = reverse_lazy("reservation:reservation")

    def form_valid(self, form):
        new_reservate = form.save(commit=False)
        new_reservate.owner = self.request.user
        new_reservate.save()
        super().form_valid(form)
        return redirect("/")


class AboutRestoTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "reservation/about_restaurant.html"


class ContactsTemplateView(TemplateView):
    template_name = "reservation/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            save_feedback(
                name=request.POST.get("name"),
                phone=request.POST.get("phone"),
                message=request.POST.get("message"),
            )
        return HttpResponseRedirect(reverse("reservation:contacts"))
