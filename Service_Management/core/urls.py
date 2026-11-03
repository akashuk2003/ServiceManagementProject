from django.urls import path
from .views import ServiceListCreateView, ServiceDetailedView

urlpatterns = [
    path('services/', ServiceListCreateView.as_view(), name="services-list"),
    path('services/<int:pk>/', ServiceDetailedView.as_view(), name="services-detail")
]
