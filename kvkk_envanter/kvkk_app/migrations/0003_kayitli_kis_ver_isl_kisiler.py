# Generated by Django 4.0.6 on 2022-08-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvkk_app', '0002_kontrol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kayitli_kis_ver_isl_kisiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kisiler', models.CharField(max_length=100)),
            ],
        ),
    ]
