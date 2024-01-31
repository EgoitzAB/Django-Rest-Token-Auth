from .models import Receta, RecetaFavorita
from rest_framework import serializers

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'

class RecetaFavoritaSerializer(serializers.ModelSerializer):

    receta = RecetaSerializer()

    class Meta:
        model = RecetaFavorita
        fields = ['receta']