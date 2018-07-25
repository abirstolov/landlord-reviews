# Generated by Django 2.0.7 on 2018-07-25 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('apartment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('street_name', models.CharField(max_length=64)),
                ('street_number', models.PositiveSmallIntegerField()),
                ('apartment_number', models.PositiveSmallIntegerField()),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('landlord_id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('landlord_first_name', models.CharField(max_length=64)),
                ('landlord_last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=70)),
                ('maintanance_description', models.TextField(max_length=256)),
                ('maintanance_rating', models.PositiveSmallIntegerField()),
                ('contract_description', models.TextField(max_length=256)),
                ('contract_rating', models.PositiveSmallIntegerField()),
                ('contact_start', models.DateField()),
                ('contract_end', models.DateField(null=True)),
                ('is_contract_ended', models.BooleanField()),
                ('rent_rate_monthly', models.SmallIntegerField(null=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lr.Apartment')),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lr.Landlord')),
            ],
        ),
        migrations.CreateModel(
            name='Tenent',
            fields=[
                ('tenent_id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('tenent_first_name', models.CharField(max_length=64)),
                ('tenent_last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='tenent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lr.Tenent'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('landlord', 'tenent', 'apartment')},
        ),
    ]