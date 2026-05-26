from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
from .models import ESGData

class ESGDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ESGData
        fields = '__all__'