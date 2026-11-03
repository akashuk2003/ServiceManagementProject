from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ServiceSerializer
from .models import Services


class ServiceListCreateView(ListCreateAPIView):
    serializer_class=ServiceSerializer

    def get_queryset(self):
        query_set=Services.objects.all().order_by("-created_at")
        
        name=self.request.query_params.get("name")

        if name is not None:
            query_set=query_set.filter(service_name__icontains=name)
        
        status=self.request.query_params.get("status")

        if status is not None:
            query_set=query_set.filter(status__iexact=status)

        return query_set


class ServiceDetailedView(RetrieveUpdateDestroyAPIView):
    queryset=Services.objects.all()
    serializer_class=ServiceSerializer
    

    