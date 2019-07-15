from rest_framework import generics

from App import models, serializers

from django.contrib.auth import get_user_model

Account = get_user_model()


class StepList(generics.ListCreateAPIView):
    queryset = models.Step.objects.all()
    serializer_class = serializers.StepSerializer


class StepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Step.objects.all()
    serializer_class = serializers.StepSerializer


class IngredientList(generics.ListCreateAPIView):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipieSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipieSerializer


class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserRecipeList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RecipieSerializer

    def get_queryset(self):
        user_pk = self.kwargs['pk']
        queryset = models.Recipe.objects.filter(user=user_pk)
        return queryset


class IngredientRecipe(generics.ListCreateAPIView):
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self):
        recipe_pk = self.kwargs['pk']
        queryset = models.Ingredient.objects.filter(recipe=recipe_pk)
        print(queryset)
        return queryset
