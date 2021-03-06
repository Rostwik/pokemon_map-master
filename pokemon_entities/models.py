from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    image = models.ImageField(blank=True, verbose_name='Изображение Покемона')
    description = models.TextField(blank=True, verbose_name='Описание')
    title_en = models.CharField(
        max_length=100, blank=True, verbose_name='Наименование англ.'
    )
    title_jp = models.CharField(
        max_length=100, blank=True, verbose_name='Наименование яп.'
    )
    previous_evolution = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_evolution',
        verbose_name='Эволюция Покемона'
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Покемон',
        related_name='entities')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        null=True, blank=True, verbose_name='Дата и время появляения'
    )
    disappeared_at = models.DateTimeField(
        null=True, blank=True, verbose_name='Дата и время исчезновения'
    )
    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(
        null=True, blank=True, verbose_name='Здоровье'
    )
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(
        null=True, blank=True, verbose_name='Выносливость'
    )
