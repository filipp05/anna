# Generated by Django 3.0.7 on 2021-02-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210228_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='anna',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='girlz_photos', verbose_name='Фото леди'),
        ),
    ]
