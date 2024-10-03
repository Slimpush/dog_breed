from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controllers import BreedDetail, BreedList, DogDetail, DogList

app_name = "api"

router = DefaultRouter()

router.register(r'breeds', BreedList, basename='breed-list')
router.register(r'breeds', BreedDetail, basename='breed-detail')

urlpatterns = [
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
    path('', include(router.urls)),
]
