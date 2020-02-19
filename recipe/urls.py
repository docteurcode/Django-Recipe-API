from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagApiView, IngredientApiView, RecipeApiView


router = DefaultRouter()
router.register('tags', TagApiView)
router.register('ingredients', IngredientApiView)
router.register('recipes', RecipeApiView)

app_name = 'recipe'

urlpatterns = [
    path("", include(router.urls))
]
