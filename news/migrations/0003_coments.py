# Generated by Django 3.2.16 on 2023-12-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_actor_kino_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Коментарий')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Коментарий ',
                'verbose_name_plural': 'Коментарий',
                'ordering': ['-time_create'],
            },
        ),
    ]
