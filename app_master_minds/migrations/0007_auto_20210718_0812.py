# Generated by Django 2.2 on 2021-07-18 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_master_minds', '0006_auto_20210716_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_quizzes', to='app_master_minds.User'),
        ),
    ]
