# Generated by Django 4.0.3 on 2022-03-18 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.topic'),
        ),
    ]
