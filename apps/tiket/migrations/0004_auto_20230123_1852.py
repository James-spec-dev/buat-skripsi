# Generated by Django 3.2.16 on 2023-01-23 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tiket', '0003_auto_20230123_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movestate',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
