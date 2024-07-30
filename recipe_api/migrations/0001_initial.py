# Generated by Django 5.0.7 on 2024-07-18 00:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('oririnCountry', models.CharField(max_length=150)),
                ('urlImag', models.CharField(max_length=250)),
                ('descriction', models.TextField()),
                ('instruction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('unitMeasure', models.CharField(max_length=10)),
                ('ingredientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_api.ingredient')),
                ('recipeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_api.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='TypeIngredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('TypeName', models.CharField(max_length=200)),
                ('ingredientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TypeIngredient', to='recipe_api.ingredient')),
            ],
        ),
    ]
