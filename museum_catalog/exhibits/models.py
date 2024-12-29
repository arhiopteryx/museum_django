from django.db import models

class Exhibit(models.Model):
    title = models.CharField(max_length=200)
    culture = models.CharField(max_length=100)
    date = models.CharField(max_length=100)  # Мы можем использовать DateField, но для упрощения возьмем CharField

    def __str__(self):
        return self.title