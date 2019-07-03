from rest_framework import serializers
from .models import Recipe


class RecipeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id', 'slug', 'name', 'final_gravity_plato', 'original_gravity_plato', 'final_gravity_sg', 'original_gravity_sg', 'style', 'difficulty', 'hop_type', 'short_description', 'long_description', 'ingredients', 'mash_time', 'boil_time', 'abv')





class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id', 'slug', 'name', 'final_gravity_plato', 'original_gravity_plato', 'final_gravity_sg', 'original_gravity_sg', 'style', 'difficulty', 'hop_type', 'short_description', 'long_description', 'ingredients', 'mash_time', 'boil_time', 'abv')
