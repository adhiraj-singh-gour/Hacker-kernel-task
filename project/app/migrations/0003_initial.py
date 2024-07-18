# Generated by Django 5.0.7 on 2024-07-18 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_remove_book_author_remove_borrowrecord_book_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField()),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowRecord',
            fields=[
                ('user_name', models.CharField(max_length=255)),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField()),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book')),
            ],
        ),
    ]
