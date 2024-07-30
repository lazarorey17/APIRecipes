from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import RecipeSerializer
from .serializer import IngredientSerializer
from .serializer import RecipeIngredientSerializer
from .serializer import GetAllRecipeIngredientSerializer

from .models import Recipe
from .models import Ingredient
from .models import RecipeIngredients
from .models import RecipeIngredients as RecipeIngredientsAux 

from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

class RecipeView(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
 
class IngredientView(ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
 
 
class RecipeIngredients(ModelViewSet):
    queryset = RecipeIngredients.objects.all()
    serializer_class = RecipeIngredientSerializer 

class RecipeByName(ModelViewSet):
    serializer_class = RecipeSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Recipe.objects.all()
        searchname = self.request.query_params.get('searchname', None)
        if searchname is not None:
            queryset = queryset.filter(name__icontains=searchname)
        return queryset
    
class RecipeByIngredients(ModelViewSet):
    serializer_class = GetAllRecipeIngredientSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = RecipeIngredientsAux.objects.all()
        recid = self.request.query_params.get('recid', None)
        if recid is not None:
            queryset = queryset.filter(recipeId=recid)
        return  queryset

    
    


    


