from django.forms import ModelForm
from django.contrib.auth.models import User
from .views import Room

class RoomForm(ModelForm):
     class Meta:
        model = Room
        fields = ['name','description','topic']

class UserForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email']