# Generated by Django 5.0.1 on 2024-01-09 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0010_movie_customer_profile_alter_customerprofile_avatar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_image.jpg', upload_to='media/')),
                ('customer_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ottapp.customerprofile')),
            ],
        ),
    ]
