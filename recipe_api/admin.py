from django.contrib import admin
from .models import Recipe
from .models import Ingredient
from .models import TypeIngredient
from .models import RecipeIngredients

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(TypeIngredient)
admin.site.register(RecipeIngredients)
