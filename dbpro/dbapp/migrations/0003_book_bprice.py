# Generated by Django 3.2.12 on 2023-07-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0002_book_bdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bprice',
            field=models.IntegerField(default=740),
        ),
    ]
