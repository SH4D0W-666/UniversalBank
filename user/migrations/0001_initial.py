# Generated by Django 3.1 on 2021-08-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('bal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200, null=True)),
                ('reciever', models.CharField(max_length=200, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
