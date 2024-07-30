from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from recipe_api import views
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'recipes', views.RecipeView)
router.register(r'ingredients',views.IngredientView)
router.register(r'recipeIngredients',views.RecipeIngredients)
router.register(r'recipebyname',views.RecipeByName,'recipebyname')
router.register(r'getrecipeingredients',views.RecipeByIngredients,'getrecipeingredients')

urlpatterns = [
    path('apirecipe/', include(router.urls)),
    path('docs/', include_docs_urls(title="Recipes API")),
]