# Generated by Django 4.1 on 2022-08-30 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kvkk_app', '0005_alter_tum_envanter_alici_gruplari_dis_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Aciklamalar',
        ),
        migrations.DeleteModel(
            name='Guvenlik_Tedbirleri',
        ),
        migrations.DeleteModel(
            name='Hukuksal_Dayanak',
        ),
        migrations.DeleteModel(
            name='Islenen_Veriler',
        ),
        migrations.DeleteModel(
            name='kontrol',
        ),
        migrations.DeleteModel(
            name='Organizasyon',
        ),
        migrations.DeleteModel(
            name='Saklama',
        ),
        migrations.DeleteModel(
            name='Surec',
        ),
        migrations.DeleteModel(
            name='users_details',
        ),
        migrations.DeleteModel(
            name='Yurtdisi_Aktarim',
        ),
        migrations.DeleteModel(
            name='Yurtici_Aktarim',
        ),
    ]
