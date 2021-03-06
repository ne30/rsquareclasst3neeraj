# Generated by Django 3.0.2 on 2020-01-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_rsquareuser_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('GEN', 'General'), ('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC')], default='GEN', max_length=4)),
                ('aadhar_num', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('address', models.CharField(max_length=200)),
                ('landmark', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=8)),
                ('school', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='rsquareuser',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=6),
        ),
    ]
