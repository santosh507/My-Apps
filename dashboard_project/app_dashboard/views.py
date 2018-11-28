from django.shortcuts import render
from rest_framework import viewsets
from .models import EmployeeDetails,SkillSet
from .serializers import EmployeeDetailsSerializers,SkillSetSerializers

# Create your views here.
class EmployeeDetailsViewSets(viewsets.ModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializers

class SkillSetViewSets(viewsets.ModelViewSet):
    queryset = SkillSet.objects.all()
    serializer_class = SkillSetSerializers