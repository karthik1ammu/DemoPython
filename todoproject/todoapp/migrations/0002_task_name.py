# Generated by Django 4.1.6 on 2023-02-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]
