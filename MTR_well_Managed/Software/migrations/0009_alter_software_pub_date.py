# Generated by Django 5.1.5 on 2025-04-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Software', '0008_remove_software_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
