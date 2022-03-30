from django.forms import ModelForm
from .views import Room, User

class RoomForm(ModelForm):
     class Meta:
        model = Room
        fields = ['name','description','topic']

class UserForm(ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email', 'bio', 'name', 'avatar']