# Generated by Django 2.2 on 2021-07-16 03:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_master_minds', '0005_auto_20210716_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='answer',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='question',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_all_quizzes', to='app_master_minds.User'),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
