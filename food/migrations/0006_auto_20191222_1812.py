# Generated by Django 3.0.1 on 2019-12-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20191222_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=400),
        ),
    ]
