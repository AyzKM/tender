# Generated by Django 3.2.5 on 2021-08-01 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0002_alter_tender_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='winner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenders.participants'),
        ),
        migrations.DeleteModel(
            name='Winner',
        ),
    ]