from rest_framework import serializers

from .models import Bitcoin

class BitcoinSerializer (serializers.Serializer):
    timestamp = serializers.DateTimeField
    price = serializers.FloatField
