from dataclasses import field
from pyexpat import model
from django.forms import ModelForm

from .views import Room

class RoomForm(ModelForm):
     class Meta:
        model = Room
        fields = ['name','description','topic']