# Generated by Django 5.1.5 on 2025-04-06 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id_sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
