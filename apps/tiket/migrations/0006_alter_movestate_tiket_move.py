# Generated by Django 3.2.16 on 2023-01-23 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiket', '0005_alter_mahasiswa_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movestate',
            name='tiket_move',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiket.tiketmodel'),
        ),
    ]
