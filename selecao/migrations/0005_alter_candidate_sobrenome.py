# Generated by Django 3.2 on 2021-04-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selecao', '0004_alter_contact_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='sobrenome',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
