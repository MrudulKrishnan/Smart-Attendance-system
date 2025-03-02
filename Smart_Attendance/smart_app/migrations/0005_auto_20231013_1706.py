# Generated by Django 3.2.20 on 2023-10-13 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smart_app', '0004_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='LOGIN_ID',
        ),
        migrations.AddField(
            model_name='attendance',
            name='STUDENT_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='smart_app.student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='COLLEGE',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='smart_app.college'),
            preserve_default=False,
        ),
    ]
