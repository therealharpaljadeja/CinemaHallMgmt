# Generated by Django 2.1.1 on 2018-10-02 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_management', '0010_auto_20181002_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.TimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name_plural': 'Movies'},
        ),
        migrations.AlterModelOptions(
            name='screens',
            options={'verbose_name_plural': 'Screens'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name_plural': 'Staff'},
        ),
        migrations.AddField(
            model_name='showtime',
            name='Movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Movies'),
        ),
        migrations.AddField(
            model_name='showtime',
            name='Screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Screens'),
        ),
    ]
