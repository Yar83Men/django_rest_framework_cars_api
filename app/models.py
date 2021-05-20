from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    vin = models.CharField(max_length=100, db_index=True, verbose_name='Вин номер')
    color = models.CharField(max_length=64, verbose_name='Цвет')
    brand = models.CharField(max_length=100, verbose_name="Модель авто")
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хетчбэк'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    car_type = models.IntegerField(max_length=100, verbose_name="Тип авто", choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)



