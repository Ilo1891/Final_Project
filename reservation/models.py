from django.core.exceptions import ValidationError
from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Table(models.Model):
    table = models.IntegerField(
        primary_key=True, help_text="Укажите номер стола", verbose_name="Номер стола"
    )
    seats = models.IntegerField(
        help_text="Количество мест", verbose_name="Количество мест"
    )
    min_people = models.IntegerField(
        help_text="Введите минимальное количество людей",
        verbose_name="Минимум человек",
        **NULLABLE,
    )
    max_people = models.IntegerField(
        help_text="Введите максимальное количество людей",
        verbose_name="Максимум человек",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="reservation/", verbose_name="Изображение", **NULLABLE
    )

    class Meta:
        verbose_name = "Стол"
        verbose_name_plural = "Столы"

    def __str__(self):
        return f"{self.table}"


class Reservation(models.Model):
    first_name = models.CharField(
        max_length=200, help_text="Укажите Имя", verbose_name="Имя", **NULLABLE
    )
    last_name = models.CharField(
        max_length=200, help_text="Укажите Фамилию", verbose_name="Фамилия", **NULLABLE
    )
    email = models.EmailField(verbose_name="Ваш email", **NULLABLE)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, verbose_name="Номер стола", **NULLABLE
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    time_reserved = models.TimeField(
        help_text="Укажите время", verbose_name="Время бронирования", **NULLABLE
    )
    date_reserved = models.DateField(
        help_text="Укажите дату", verbose_name="Дата бронирования", **NULLABLE
    )
    is_booked = models.BooleanField(default=False, verbose_name="Признак брони")

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирование"

        constraints = [
            models.UniqueConstraint(
                fields=["time_reserved", "date_reserved", "table"],
                name="name of constraint",
            )
        ]

        def __str__(self):
            return f"Стол номер {self.table}, клиент {self.first_name} {self.last_name}, {self.owner}"
