# Generated by Django 3.0.1 on 2019-12-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='food',
            name='categories',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
