# Generated by Django 4.2 on 2023-04-26 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preoccupation',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mocta1', to='core.utilisateurs'),
        ),
        migrations.AlterField(
            model_name='preoccupation',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mocta2', to='core.utilisateurs'),
        ),
        migrations.AlterField(
            model_name='reponse',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mocta3', to='core.utilisateurs'),
        ),
        migrations.AlterField(
            model_name='reponse',
            name='poste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mocta4', to='core.utilisateurs'),
        ),
        migrations.AlterField(
            model_name='reponsecompetition',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mocta5', to='core.utilisateurs'),
        ),
    ]
