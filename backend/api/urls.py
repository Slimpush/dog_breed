from django.urls import path
from rest_framework.routers import DefaultRouter
from controllers import BreedDetail, BreedList, DogList, DogDetail


router = DefaultRouter()

router.register(r'breeds', BreedList, basename='breed-list')
router.register(r'breeds', BreedDetail, basename='breed-detail')

urlpatterns = [
    path('dogs/', DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', DogDetail.as_view(), name='dog-detail'),
]

urlpatterns += router.urls
