# Generated by Django 4.0.3 on 2022-03-24 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-create_at']},
        ),
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
    ]
