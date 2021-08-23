# Generated by Django 3.2.6 on 2021-08-20 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rgd', '0002_alter_spatialasset_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='checksumfile',
            name='created_by',
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
