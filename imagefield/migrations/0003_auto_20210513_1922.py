# Generated by Django 3.2.2 on 2021-05-13 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagefield.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imagefield', '0002_delete_getimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='images/')),
                ('hash', imagefield.models.PositiveBigIntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.DeleteModel(
            name='ImagefieldModel',
        ),
    ]
