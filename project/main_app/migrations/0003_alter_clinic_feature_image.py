# Generated by Django 4.2.2 on 2023-06-10 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_clinic_doctor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='feature_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
