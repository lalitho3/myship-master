# Generated by Django 4.1.3 on 2022-11-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('foto', models.ImageField(upload_to='fotos/', verbose_name='Foto')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-fecha'],
            },
        ),
    ]