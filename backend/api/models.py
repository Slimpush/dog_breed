from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


RATING_VALIDATORS = [MinValueValidator(1), MaxValueValidator(5)]


class Breed(models.Model):
    SIZE_TINY = "tiny"
    SIZE_SMALL = "small"
    SIZE_MEDIUM = "medium"
    SIZE_LARGE = "large"

    SIZE_CHOICES = [
        (SIZE_TINY, "крошечная"),
        (SIZE_SMALL, "маленькая"),
        (SIZE_MEDIUM, "средняя"),
        (SIZE_LARGE, "большая"),
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название породы",
    )
    size = models.CharField(
        max_length=20,
        choices=SIZE_CHOICES,
        verbose_name="Размер собаки",
    )
    friendliness = models.IntegerField(
        validators=RATING_VALIDATORS,
        verbose_name="Дружелюбность (от 1 до 5)",
    )
    trainability = models.IntegerField(
        validators=RATING_VALIDATORS,
        verbose_name="Обучаемость (от 1 до 5)",
    )
    shedding_amount = models.IntegerField(
        validators=RATING_VALIDATORS,
        verbose_name="Количество шерсти при линьке (от 1 до 5)",
    )
    exercise_needs = models.IntegerField(
        validators=RATING_VALIDATORS,
        verbose_name="Потребность в активности (от 1 до 5)",
    )

    class Meta:
        verbose_name = "Порода собаки"
        verbose_name_plural = "Породы собак"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Dog(models.Model):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = [
        (GENDER_MALE, "мужской"),
        (GENDER_FEMALE, "женский"),
    ]

    name = models.CharField(
        max_length=50,
        verbose_name="Имя собаки",
    )
    age = models.IntegerField(
        verbose_name="Возраст собаки",
    )
    breed = models.ForeignKey(
        Breed,
        verbose_name="Порода собаки",
        related_name="breed",
        null=True,
        on_delete=models.SET_NULL,
    )
    gender = models.CharField(
        max_length=10,
        verbose_name="Пол собаки",
        choices=GENDER_CHOICES,
    )
    color = models.CharField(
        max_length=30,
        verbose_name="Окрас собаки",
    )
    favorite_food = models.CharField(
        max_length=100,
        verbose_name="Любимая еда",
    )
    favorite_toy = models.CharField(
        max_length=100,
        verbose_name="Любимая игрушка",
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} - собака породы {self.breed.name}."
