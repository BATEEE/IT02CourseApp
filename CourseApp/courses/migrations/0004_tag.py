# Generated by Django 5.1.6 on 2025-02-21 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('lesson', models.ManyToManyField(to='courses.lesson')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
