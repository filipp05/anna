from django.db import models


class Anna(models.Model):
    SCHOOL_GIRL_TYPES = [("Босс", "Босс"), ("Спортивная рота", "Спортивная рота"),
                         ("Медицинский отряд", "Медицинский отряд"), ("Наукоград", "Наукоград"),
                         ("Кулинарный колледж", "Кулинарный колледж")]
    name = models.CharField(verbose_name="Имя", max_length=20, default="Аня")
    surname = models.CharField(verbose_name="Фамилияя", max_length=20, default="Зверева")
    photo = models.ImageField(upload_to="girlz_photos", height_field=None, width_field=None, verbose_name="Фото леди",
                              null=True, blank=True)
    xp = models.IntegerField(default=1)
    description = models.TextField("Описание")
    type1 = models.CharField(verbose_name="Тип", max_length=150, choices=SCHOOL_GIRL_TYPES, default="СР")

    def __str__(self):
        return str(self.name + " " + self.surname)
