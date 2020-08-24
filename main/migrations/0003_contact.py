# Generated by Django 3.0.5 on 2020-08-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200728_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.TextField(blank=True, max_length=100, null=True)),
                ('lname', models.TextField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField()),
                ('sub', models.TextField(blank=True, max_length=500, null=True)),
                ('msg', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
