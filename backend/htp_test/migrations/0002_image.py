# Generated by Django 4.2.5 on 2023-09-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htp_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
