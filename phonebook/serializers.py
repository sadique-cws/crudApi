from rest_framework import serializers
from .models import Vcard

class VcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vcard
        fields = "__all__"
        