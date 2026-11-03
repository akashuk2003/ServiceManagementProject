from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

from .models import Services
from .forms import ServiceForm


class ServiceListView(ListView):
    model=Services
    template_name="service_list.html"
    context_object_name="services"
    paginate_by=5

    def get_queryset(self):
        query_set=Services.objects.all().order_by("-created_at")

        name=self.request.GET.get("name")
        status=self.request.GET.get("status")

        if name:
            query_set=query_set.filter(service_name__icontains=name.strip())

        if status:
            query_set=query_set.filter(status__iexact=status.strip())

        return query_set

class ServiceCreateView(CreateView):
    model=Services
    form_class= ServiceForm
    template_name="service_form.html"
    success_url = reverse_lazy("service_list")

class ServiceDetailView(DetailView):
    model = Services
    template_name = "service_detail.html"
    context_object_name = "service"
    success_url = reverse_lazy("service_list")

class ServiceUpdateView(UpdateView):
    model=Services
    form_class=ServiceForm
    template_name="service_form.html"
    success_url = reverse_lazy("service_list")

class ServiceDeleteView(DeleteView):
    model=Services
    template_name="service_confirm_delete.html"
    success_url = reverse_lazy("service_list")
