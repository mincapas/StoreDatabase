# Generated by Django 4.0.6 on 2022-08-22 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeDatabase', '0018_reviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Atsiliepimas', 'verbose_name_plural': 'Atsiliepimai'},
        ),
        migrations.AlterField(
            model_name='recipesitem',
            name='text',
            field=models.TextField(help_text='Recepto aprasymas', max_length=2000, verbose_name='Recepto aprasymas'),
        ),
    ]
