from django.db import models
import uuid

# Create your models here.

class Recipe(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=200)
    oririnCountry = models.CharField(max_length=150)
    urlImag = models.CharField(max_length=250)
    descriction = models.TextField(blank=False)
    instruction = models.TextField(blank=False)

  
class Ingredient(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=200)

class TypeIngredient(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    TypeName = models.CharField(max_length=200)

    ingredientId = models.ForeignKey(
        "Ingredient",
        on_delete=models.CASCADE,
        related_name="TypeIngredient",
        null=False
    )

class RecipeIngredients(models.Model):
    recipeId=models.ForeignKey(
        "Recipe",
        on_delete=models.CASCADE,
        null=False
    )
    ingredientId = models.ForeignKey(
        "Ingredient",
        on_delete=models.CASCADE,
        null=False
    )

    count = models.IntegerField()
    unitMeasure = models.CharField(max_length=10)