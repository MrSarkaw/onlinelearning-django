# Generated by Django 4.0.3 on 2022-03-24 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_room_options_remove_message_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-create_at']},
        ),
    ]