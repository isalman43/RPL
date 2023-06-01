# Generated by Django 4.2.1 on 2023-06-01 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0005_alter_tabelnon_nip_alter_tabelsiswa_nis'),
        ('pinjam', '0002_remove_tabelpinjams_judul_tabelpinjamn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelpinjamn',
            name='no_anggotaN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anggota.tabelnon'),
        ),
        migrations.AlterField(
            model_name='tabelpinjams',
            name='no_anggota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anggota.tabelsiswa'),
        ),
    ]
