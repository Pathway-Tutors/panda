# Generated by Django 5.2 on 2025-04-20 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_application_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecisionReason',
            fields=[
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.application')),
                ('reason', models.TextField(max_length=1785)),
            ],
        ),
    ]
