from .views import ProductViewSet, CategoryViewSet
from django.urls import path


app_name = 'product'

urlpatterns = [
    path('product/<str:slug>/', ProductViewSet.as_view(), name='product'),
    path('product/', ProductViewSet.as_view()),
    path('category/', CategoryViewSet.as_view()),
]
