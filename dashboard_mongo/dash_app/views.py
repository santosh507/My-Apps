from django.shortcuts import render
from .serializers import CustomerDetailsSerializer
from .models import CustomerDetails

# Create your views here.
from rest_framework_mongoengine import viewsets

class CustomerDetailsViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    #queryset = Tool.objects.all()
    lookup_field = 'id'
    serializer_class = CustomerDetailsSerializer


    def get_queryset(self):
        return CustomerDetails.objects.all()
