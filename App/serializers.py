from rest_framework import serializers, exceptions
import django.contrib.auth.password_validation as validators
from App.models import Ingredient, Step, Recipe, User

#a little changes
#hello world added
class IngredientSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Ingredient
        fields = ('text', 'recipe')


class StepSerializer(serializers.ModelSerializer, ):
    class Meta:
        model = Step
        fields = ('step_text', 'recipe',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # recipes = RecipieSerializer(source='user_recipe', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email',)

    def validate(self, data):
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(UserSerializer, self).validate(data)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.username = validated_data['username']
        user.set_password(validated_data['password'])
        user.email = validated_data['email']
        user.save()
        return user

    def update(self, instance, validated_data):
        user = validated_data.get('user')
        instance.password = user.get('password')
        instance.email = user.get('email')
        instance.first_name = user.get('first_name')
        instance.last_name = user.get('last_name')
        instance.save()
        return instance


class RecipieSerializer(serializers.ModelSerializer, ):
    # user = UserSerializer()
    ingredients = IngredientSerializer(source='ingredient_recipe', many=True, read_only=True, )
    steps = StepSerializer(source='step_recipe', many=True, read_only=True, )

    class Meta:
        model = Recipe

        fields = ('user', 'name', 'steps', 'ingredients',)
