# Generated by Django 4.2.1 on 2023-06-01 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam', '0002_remove_tabelpinjams_judul_tabelpinjamn'),
        ('kembali', '0002_tabelkembalin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelkembalin',
            name='noPinjamN',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pinjam.tabelpinjamn'),
        ),
        migrations.AlterField(
            model_name='tabelkembalis',
            name='noPinjamS',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pinjam.tabelpinjams'),
        ),
    ]
