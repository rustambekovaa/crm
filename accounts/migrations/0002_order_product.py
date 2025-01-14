# Generated by Django 5.0.2 on 2024-04-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for deliver', 'Out for deliver'), ('Deliver', 'deliver')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phprice', models.IntegerField(max_length=200)),
                ('category', models.CharField(max_length=200, null=True)),
                ('description', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
