from rest_framework import serializers
from .models import EmployeeDetails,SkillSet

class EmployeeDetailsSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = EmployeeDetails
        fields = '__all__'
        depth = 1

class SkillSetSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = SkillSet
        fields = '__all__'