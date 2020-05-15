# Generated by Django 3.0.3 on 2020-03-18 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excuseTypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledReasons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='emergency',
            name='CSU_ID',
            field=models.CharField(default=0, max_length=999999999),
        ),
        migrations.AddField(
            model_name='emergency',
            name='fullName',
            field=models.CharField(default='error', max_length=100),
        ),
        migrations.AddField(
            model_name='emergency',
            name='shortDesc',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Scheduled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='error', max_length=100)),
                ('CSU_ID', models.CharField(default=0, max_length=999999999)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('shortDesc', models.TextField(blank=True)),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excuseTypes.ScheduledReasons')),
            ],
        ),
    ]