from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории', max_length=500, blank=True)
    description = models.CharField('Описание категории', max_length=500, blank=True)

    def __str__(self):

        return str(self.name)

    class Meta:

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Shoes(models.Model):

    name = models.CharField('Название обуви', max_length=500, blank=True)
    description = models.CharField('Описание обуви', max_length=500, blank=True)
    date = models.DateTimeField("Дата", blank=True, null=True)
    price = models.PositiveIntegerField("Цена", blank=True)
    size = models.PositiveIntegerField("Размер", blank=True)
    color = models.CharField('Цвет обуви', max_length=500, blank=True)
    image = models.ImageField("Image", upload_to='media/photo', blank=True)
    image_2 = models.ImageField("Image", upload_to='photo', blank=True)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обувь'


class Zayavka(models.Model):

    name = models.CharField('ФИО', max_length=500, blank=True)
    shoes_name = models.CharField('Название обуви', max_length=500, blank=True)
    size = models.CharField('Размер обуви', max_length=500, blank=True)
    number = models.CharField('Номер телефона', max_length=500, blank=True)
    adress = models.CharField('Адрес доставки', max_length=500, blank=True)


    def __str__(self):

        return "{}  на имя {}".format(self.shoes_name, self.name)

    class Meta:

        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

