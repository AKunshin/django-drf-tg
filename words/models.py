from django.db import models


class Word(models.Model):

    GENDERS = [
        ('mas', 'Masculine'),
        ('fem', 'Feminine'),
        ('neu', 'Neuter'),
    ]

    word = models.CharField(max_length=100, verbose_name="Word")
    gender = models.CharField(
        choices=GENDERS, max_length=10, verbose_name="Gender")

    def __str__(self):
        return self.gender + " " + self.word