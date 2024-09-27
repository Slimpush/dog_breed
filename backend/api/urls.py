from django.urls import path

from .controllers import BreedDetail, BreedList, DogDetail, DogList

app_name = "api"

urlpatterns = [
    path("dogs/", DogList.as_view(), name="dog-list"),
    path("dogs/<int:pk>/", DogDetail.as_view(), name="dog-detail"),
    path(
        "breeds/", BreedList.as_view({"get": "get", "post": "post"}), name="breed-list"
    ),
    path(
        "breeds/<int:pk>/",
        BreedDetail.as_view({"get": "get", "put": "put", "delete": "delete"}),
        name="breed-detail",
    ),
]
