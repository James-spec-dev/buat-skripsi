# Generated by Django 3.2.16 on 2023-01-23 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiket', '0002_auto_20230123_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiketmodel',
            name='status',
        ),
        migrations.AddField(
            model_name='movestate',
            name='tiket_move',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tiket.tiketmodel'),
        ),
    ]