# Generated by Django 2.1.1 on 2018-11-02 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181102_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(default='default.jpg', on_delete=django.db.models.deletion.PROTECT, to='images.Image'),
        ),
    ]
