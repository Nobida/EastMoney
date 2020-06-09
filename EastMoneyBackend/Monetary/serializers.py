from rest_framework import serializers
from Monetary.models import Monetary

class MonetarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monetary
        fields = '__all__'

