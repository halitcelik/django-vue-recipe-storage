from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.views.generic.edit import FormView
from .forms import RecipeForm
from .models import Recipe
from .renderers import RecipeJSONRenderer
from .serializers import RecipeSerializer, RecipeListSerializer


class RecipeListApiView(ListCreateAPIView):
    model = Recipe
    queryset = Recipe.objects.all()
    permission_classes = (AllowAny,)
    renderer_classes = (RecipeJSONRenderer,)
    serializer_class = RecipeListSerializer


class RecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    permission_classes = (AllowAny, )
    queryset = Recipe.objects.all()
    renderer_classes = (RecipeJSONRenderer, )
    serializer_class = RecipeSerializer

    def retrieve(self, request, id, *args, **kwargs):
        recipe = Recipe.objects.get(id=id)
        serializer = self.serializer_class(recipe)

        return Response(serializer.data, status=status.HTTP_200_OK)




class RecipeView(FormView):
    template_name = 'home.html'
    form_class = RecipeForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
