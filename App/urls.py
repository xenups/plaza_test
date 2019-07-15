from django.urls import path, include

from App.views import RecipeList, RecipeDetail, StepList, StepDetail, IngredientDetail, IngredientList, UserRecipeList, \
    UserList, UserDetail, IngredientRecipe

urlpatterns = [
    path('recipe/', RecipeList.as_view()),
    path('recipe/<int:pk>', RecipeDetail.as_view()),

    path('userrecipe/<int:pk>', UserRecipeList.as_view()),
    path('recipiesingredients/<int:pk>', IngredientRecipe.as_view()),

    path('step/', StepList.as_view()),
    path('step/<int:pk>', StepDetail.as_view()),

    path('ingredient/', IngredientList.as_view()),
    path('ingredient/<int:pk>', IngredientDetail.as_view()),

    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),

    # path('books/<int:pk>/', views.BookDetail.as_view()),

]
