# Generated by Django 4.2.8 on 2024-01-17 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samochod', '0005_part_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='part',
            name='mark',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='samochod.mark'),
        ),
    ]
