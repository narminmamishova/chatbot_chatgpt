# Generated by Django 4.2.9 on 2024-02-07 22:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_chatbot_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
