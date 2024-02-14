from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room #model = obiekt który chcesz stworzyć
        fields = '__all__'
        exclude = ['host', 'participants']