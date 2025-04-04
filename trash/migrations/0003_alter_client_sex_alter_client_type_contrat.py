# Generated by Django 4.2.5 on 2025-02-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0002_client_date_paiement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='sex',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin'), ('O', 'Autre')], max_length=1),
        ),
        migrations.AlterField(
            model_name='client',
            name='type_contrat',
            field=models.CharField(choices=[('1', 'Contrat Type 1'), ('2', 'Contrat Type 2'), ('3', 'Contrat Type 3')], max_length=1),
        ),
    ]
