from rest_framework import serializers
from .models import Subsitema

class SubsitemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsitema
        fields = '__all__'
