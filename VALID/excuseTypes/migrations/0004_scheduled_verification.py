# Generated by Django 3.0.4 on 2020-03-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excuseTypes', '0003_auto_20200318_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduled',
            name='Verification',
            field=models.FileField(default=False, upload_to='verifyDocs/'),
        ),
    ]
