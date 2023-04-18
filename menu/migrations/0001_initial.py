# Generated by Django 4.0.3 on 2023-04-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='메뉴명')),
                ('price', models.IntegerField()),
                ('info', models.TextField()),
                ('category', models.CharField(choices=[('버거', '버거'), ('사이드', '사이드'), ('디저트', '디저트'), ('음료', '음료')], max_length=5)),
                ('ss_choice', models.CharField(choices=[('단품', '단품'), ('세트', '세트')], max_length=2)),
            ],
        ),
    ]