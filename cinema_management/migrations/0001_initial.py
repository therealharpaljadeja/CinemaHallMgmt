# Generated by Django 2.1.1 on 2018-10-01 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Contact', models.ManyToManyField(to='cinema_management.CustContact')),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodStall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Rent', models.IntegerField()),
                ('Commodity', models.CharField(max_length=40)),
                ('Commodity_Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Language', models.CharField(blank=True, choices=[('Eng', 'English'), ('Hin', 'Hindi'), ('Mar', 'Marathi')], max_length=3)),
                ('Release_date', models.DateTimeField()),
                ('Runtime', models.CharField(blank=True, max_length=10)),
                ('Genre', models.CharField(blank=True, max_length=15)),
                ('Ratings', models.FloatField(default=0.0)),
                ('Certification', models.CharField(blank=True, choices=[('U', 'Universal'), ('U/A', 'Universal/Adult'), ('A', 'Adult')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Screens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Address', models.TextField()),
                ('Shift', models.CharField(choices=[('M', 'Morning'), ('N', 'Night')], max_length=1)),
                ('Designation', models.CharField(blank=True, max_length=100)),
                ('Salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.IntegerField(blank=True)),
                ('Staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Screens')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Customer')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('2d', '2D'), ('3D', '3D'), ('IMAX', 'Imax')], max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='screens',
            name='type',
            field=models.ManyToManyField(blank=True, to='cinema_management.Type'),
        ),
        migrations.AddField(
            model_name='display',
            name='Screen_number',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Screens'),
        ),
        migrations.AddField(
            model_name='display',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Movies'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Screen_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Screens'),
        ),
        migrations.AddField(
            model_name='customer',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Movies'),
        ),
        migrations.AddField(
            model_name='custcontact',
            name='Customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_management.Customer'),
        ),
    ]