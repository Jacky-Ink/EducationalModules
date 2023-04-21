from django.db import models

class EducatioalModules(models.Model):
    slug = models.SlugField(
        null=False,
        unique=True,
        verbose_name='Порядковый номер'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название образовательного модуля'
    )
    description = models.TextField(
        verbose_name='Опиасание образовательного модуля'
    )

    def __str__(self) -> str:
        return self.name
