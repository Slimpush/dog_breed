from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from dog_breed.settings import (MAX_LENGHT_COLOR, MAX_LENGHT_FAVORITE,
                                MAX_LENGTH_BREED, MAX_LENGTH_GENDER,
                                MAX_LENGTH_NAME, MAX_LENGTH_SIZE)


class Breed(models.Model):
    SIZE_CHOICES = [
        ("Tiny", "Крошечная"),
        ("Small", "Маленькая"),
        ("Mediun", "Среднего размера"),
        ("Large", "Большая"),
    ]

    name = models.CharField(
        max_length=MAX_LENGTH_BREED,
        unique=True,
        verbose_name="Название породы",
    )
    size = models.CharField(
        max_length=MAX_LENGTH_SIZE,
        choices=SIZE_CHOICES,
        verbose_name="Размер собаки",
    )
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Дружелюбность (от 1 до 5)",
    )
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Обучаемость (от 1 до 5)",
    )
    shedding_amount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Количество шерсти при линьке (от 1 до 5)",
    )
    exercise_needs = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Потребность в активности (от 1 до 5)",
    )

    class Meta:
        verbose_name = "Порода собаки"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Dog(models.Model):
    GENDER_CHOICE = [
        ("male", "мужской"),
        ("female", "женский"),
    ]

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name="Имя собаки",
    )
    age = models.IntegerField(
        verbose_name="Возраст собаки",
    )
    breed = models.ForeignKey(
        Breed,
        verbose_name="Порода собаки",
        related_name="breed",
        on_delete=models.CASCADE,
    )
    gender = models.CharField(
        max_length=MAX_LENGTH_GENDER,
        verbose_name="Пол собаки",
        choices=GENDER_CHOICE,
    )
    color = models.CharField(
        max_length=MAX_LENGHT_COLOR,
        verbose_name="Окрас собаки",
    )
    favorite_food = models.CharField(
        max_length=MAX_LENGHT_FAVORITE,
        verbose_name="Любимая еда",
    )
    favorite_toy = models.CharField(
        max_length=MAX_LENGHT_FAVORITE,
        verbose_name="Любимая игрушка",
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name} - собака породы {self.breed.name}."
