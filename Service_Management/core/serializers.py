from rest_framework import serializers
from .models import Services

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields='__all__'

        #validation
        def validate_service_name(self,value):
            value=value.strip()

            if len(value)<0:
                raise serializers.ValidationError(
                    "Service name should be atleast 3 characters"
                )

        def validate_price(self,value):
            if value<0:
                raise serializers.ValidationError(
                    "price should be greater than zero"
                )

        def validate_duration(self,value):
            if value<0:
                raise serializers.ValidationError(
                    "duration should be greater than zero"
                )