# Generated by Django 3.2.20 on 2023-10-17 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0012_auto_20231017_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='DEPARTMENT',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='smart_app.department'),
            preserve_default=False,
        ),
    ]
