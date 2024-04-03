from rest_framework import serializers
from .models import DRINKS

class serializedDrinks(serializers.ModelSerializer):
    class Meta:
        model = DRINKS
        fields = '__all__'