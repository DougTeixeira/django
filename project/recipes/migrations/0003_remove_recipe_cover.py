# Generated by Django 4.0.5 on 2022-06-27 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_category_alter_recipe_cover_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cover',
        ),
    ]