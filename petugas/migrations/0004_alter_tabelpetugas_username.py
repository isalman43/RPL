# Generated by Django 4.2.1 on 2023-06-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petugas', '0003_alter_tabelpetugas_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelpetugas',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
