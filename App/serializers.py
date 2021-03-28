from rest_framework import serializers
from .models import (
    DataM
)

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataM
        fields = ("education","marital_education","default","job","targeted","marital","housing","month")