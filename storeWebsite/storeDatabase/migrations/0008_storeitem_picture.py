# Generated by Django 4.0.6 on 2022-07-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeDatabase', '0007_websiteinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='picture',
            field=models.ImageField(null=True, upload_to='itemImages', verbose_name='Paveikslelis'),
        ),
    ]
