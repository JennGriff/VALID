# Generated by Django 3.0.4 on 2020-05-06 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excuseTypes', '0004_scheduled_verification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='Verification',
            field=models.FileField(blank=True, default=False, null=True, upload_to='verifyDocs/'),
        ),
        migrations.AddField(
            model_name='scheduled',
            name='prof',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='excuseTypes.Prof'),
            preserve_default=False,
        ),
    ]
