# Generated by Django 3.2 on 2021-04-06 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0002_contact_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='selecao.candidate'),
        ),
    ]
