from django.urls import path

from .html_views import (
    ServiceListView,
    ServiceCreateView,
    ServiceDetailView,
    ServiceUpdateView,
    ServiceDeleteView
)

urlpatterns = [
    path("services/", ServiceListView.as_view(), name="service_list"),

    path("services/create/", ServiceCreateView.as_view(), name="service_create"),

    path("services/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),

    path("services/<int:pk>/edit/", ServiceUpdateView.as_view(), name="service_update"),

    path("services/<int:pk>/delete/", ServiceDeleteView.as_view(), name="service_delete"),
]