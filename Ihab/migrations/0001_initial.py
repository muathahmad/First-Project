# Generated by Django 2.2.4 on 2019-08-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=160)),
            ],
        ),
    ]
