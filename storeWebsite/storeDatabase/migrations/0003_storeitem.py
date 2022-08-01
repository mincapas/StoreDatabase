# Generated by Django 4.0.6 on 2022-07-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeDatabase', '0002_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Prekes pavadinimas', max_length=200, verbose_name='Pavadinimas')),
                ('price', models.FloatField(help_text='Prekes kaina', verbose_name='Kaina')),
                ('description', models.TextField(help_text='Prekes aprasymas', max_length=200, verbose_name='Aprasymas')),
                ('supplier', models.ManyToManyField(help_text='parinkite galimus tiekejus siai prekei', to='storeDatabase.supplier')),
            ],
        ),
    ]