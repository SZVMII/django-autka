# Generated by Django 4.2.8 on 2024-01-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samochod', '0006_mark_alter_part_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='mark',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]
