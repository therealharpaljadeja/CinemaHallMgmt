# Generated by Django 2.1.1 on 2018-10-03 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_management', '0011_auto_20181002_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(max_length=3)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Customer')),
                ('Movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Movies')),
                ('Screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Screens')),
            ],
        ),
        migrations.AlterField(
            model_name='showtime',
            name='Time',
            field=models.TimeField(null=True),
        ),
    ]