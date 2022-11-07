# Generated by Django 4.1 on 2022-08-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvkk_app', '0004_aciklamalar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tum_envanter',
            name='alici_gruplari_dis',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='alici_gruplari_ic',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='amac',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='departman_ismi',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='erisebilen_kisiler',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='gerekli_olmayan_veriler',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='is_sureci',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='islenen_kisisel_veriler',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='islenen_sure',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='islenen_tum_veriler',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='kisisel_verinin_toplanma_yontemi',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='kisisel_verisi_islenen_kisi',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='paylasilan_ulkeler',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='paylasilan_veriler',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='paylasim_amaci',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='paylasim_amaclari',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='saklanilan_yer',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='tum_tedbirler',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='veri_isleme_faaliyeti',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tum_envanter',
            name='yetkili',
            field=models.CharField(max_length=30),
        ),
    ]