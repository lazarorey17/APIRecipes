from rest_framework import serializers
from .models import Recipe
from .models import Ingredient
from .models import RecipeIngredients
from rest_framework import request

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredients
        fields = '__all__'

class GetAllRecipeIngredientSerializer(serializers.ModelSerializer):
    recipeId = RecipeSerializer(read_only=True)
    ingredientId = IngredientSerializer(read_only=True)
    class Meta:
        model = RecipeIngredients
        fields = '__all__'; 

    

