from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField("Назва", max_length=100)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField("Назва", max_length=150)
    description = models.TextField("Опис", blank=True)
    price = models.DecimalField("Ціна, грн", max_digits=7, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="dishes",
        verbose_name="Категорія"
    )
    is_available = models.BooleanField("Є в наявності",default=True)
    created_at = models.DateTimeField("Додано" ,auto_now_add=True)

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"
        ordering = ["name"]

    def __str__(self):
        return self.name