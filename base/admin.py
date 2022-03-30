from django.contrib import admin
from .models import Room, Topic, Message, User


admin.site.register([Room, Topic, Message, User])
