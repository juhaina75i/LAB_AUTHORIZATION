# Generated by Django 4.2.2 on 2023-06-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='doctor_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
