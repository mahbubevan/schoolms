# Generated by Django 3.0.2 on 2020-01-04 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20200104_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='hire_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]