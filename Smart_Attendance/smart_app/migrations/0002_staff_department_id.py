# Generated by Django 3.2.20 on 2023-10-13 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='DEPARTMENT_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='smart_app.department'),
            preserve_default=False,
        ),
    ]
