# Generated by Django 3.2.20 on 2023-10-16 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0007_remove_department_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='smart_app.login'),
            preserve_default=False,
        ),
    ]
