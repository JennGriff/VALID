# Generated by Django 3.0.4 on 2020-05-06 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excuseTypes', '0007_auto_20200506_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergency',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excuseTypes.Prof'),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excuseTypes.Prof'),
        ),
    ]
