# Generated by Django 3.0.2 on 2020-01-10 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_course_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='manager',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
