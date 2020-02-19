from rest_framework import serializers
from .models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'user']
        read_only_fields = ['id', ]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):

    ingredient = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_miuntie',
                  'price', 'ingredient', 'tags', 'created_at']
        read_only_fields = ['id', ]


class RecipeDetailsSerializer(RecipeSerializer):
    ingredient = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_miuntie',
                  'price', 'ingredient', 'tags', 'user', 'created_at']


class RecipeImageSerializer(serializers.ModelSerializer):
    class Meta:
        models = Recipe
        fields = ['id', 'images']
        read_only_fields = ['id', ]
