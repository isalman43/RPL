# Generated by Django 4.2.1 on 2023-05-27 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0002_rename_nim_anggotasiswa_nis'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='anggotaSiswa',
            new_name='tabelSiswa',
        ),
    ]
