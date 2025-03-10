# Generated by Django 2.2.7 on 2023-06-10 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('patient_age', models.IntegerField()),
                ('discription', models.TextField(max_length=500)),
                ('phone_number', models.CharField(max_length=120)),
                ('appointment_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_attended', models.BooleanField(default=False)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Clinic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
