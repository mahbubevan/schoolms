# Generated by Django 3.0.2 on 2020-01-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
