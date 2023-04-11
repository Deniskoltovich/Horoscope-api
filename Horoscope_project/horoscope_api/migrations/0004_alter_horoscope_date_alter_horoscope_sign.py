# Generated by Django 4.1.7 on 2023-03-21 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope_api', '0003_alter_horoscope_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horoscope',
            name='date',
            field=models.DateField(default=datetime.date(2023, 3, 21)),
        ),
        migrations.AlterField(
            model_name='horoscope',
            name='sign',
            field=models.CharField(choices=[('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'), ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces')], max_length=64),
        ),
    ]
