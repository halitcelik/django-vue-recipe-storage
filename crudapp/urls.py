from django.urls import path
from .views import RecipeListApiView, RecipeRetrieveUpdateDestroyAPIView

app_name = 'recipe'

urlpatterns = [
    path('recipes/', RecipeListApiView.as_view()),
    path('recipes/<str:id>/', RecipeRetrieveUpdateDestroyAPIView.as_view()),
]
