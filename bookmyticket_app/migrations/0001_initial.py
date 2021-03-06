# Generated by Django 3.1.1 on 2020-09-05 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, choices=[('BOOKED', 'BOOKED'), ('PENDING', 'PENDING'), ('CANCEL', 'CANCEL')], max_length=128, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0)),
                ('seat_count', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('state', models.CharField(max_length=1024)),
                ('country', models.CharField(max_length=1024)),
                ('pin', models.CharField(max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('director', models.CharField(max_length=1024)),
                ('cast', models.CharField(max_length=4096)),
                ('release_date', models.DateTimeField()),
                ('duration', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=4096, null=True)),
                ('rating', models.CharField(max_length=16)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.PositiveIntegerField()),
                ('seat_no', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('audi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.audi')),
            ],
        ),
        migrations.CreateModel(
            name='SeatReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.booking')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.seat')),
            ],
        ),
        migrations.CreateModel(
            name='MovieShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('price', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('audi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.audi')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.movie')),
            ],
        ),
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.cinema')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.city')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='movie_show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.movieshow'),
        ),
        migrations.AddField(
            model_name='audi',
            name='cinema_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmyticket_app.cinemahall'),
        ),
    ]
