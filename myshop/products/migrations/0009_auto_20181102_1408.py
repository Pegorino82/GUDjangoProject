# Generated by Django 2.1.1 on 2018-11-02 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20181102_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='images.Image'),
        ),
    ]
