# Generated by Django 4.0.6 on 2022-07-27 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeDatabase', '0012_recipesitem_created_at_recipesitem_publications_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipesitem',
            old_name='publications',
            new_name='related_products',
        ),
    ]
