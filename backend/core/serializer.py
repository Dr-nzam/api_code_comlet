from rest_framework import serializers
from .models import Cours

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ['nom', 'titre','contenue','fichier']