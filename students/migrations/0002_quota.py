# Generated by Django 3.2.7 on 2021-09-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
                ('semester', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('limit', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=64)),
                ('quotas', models.ManyToManyField(blank=True, related_name='quotas', to='students.Student')),
            ],
        ),
    ]
