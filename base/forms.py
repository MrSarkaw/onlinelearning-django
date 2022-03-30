from django import forms
from .views import Room, User

class RoomForm(forms.ModelForm):
     class Meta:
        model = Room
        fields = ['name','description','topic']

class UserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ['username', 'email', 'bio', 'name', 'avatar', 'password']
      widgets = {
      'password': forms.PasswordInput()
         }