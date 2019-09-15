import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Ingredient, Recipe, UserProfile, User
from .serializers import IngredientSerializer

client = Client()


class GetAllIngredientTest(TestCase):
    def setUp(self):
        self.username = 'amirlesani'
        self.email = 'amirlesani@gmail.com'
        self.password = 'you_know_nothing'
        test_user = User.objects.create_user(self.username, self.email, self.password)
        recepe = Recipe.objects.create(user=test_user, name='daste bil')
        self.ing = Ingredient.objects.create(
            # text="daste asbe abi",
            recipe=recepe
        )
        self.ing.save()

    def test_get_all_ingredient(self):
        print('testinnng')
        # print(reverse('ingredient'))
        response = client.get('http://127.0.0.1:8000/api/ingredient/')
        ingredient = Ingredient.objects.all()
        print(ingredient.get())
        serializer_ingredient = IngredientSerializer(ingredient)
        print(serializer_ingredient.data)
        self.assertEqual(response.data, serializer_ingredient.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
