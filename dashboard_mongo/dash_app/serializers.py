from rest_framework_mongoengine import serializers
from .models import CustomerDetails

class CustomerDetailsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'
