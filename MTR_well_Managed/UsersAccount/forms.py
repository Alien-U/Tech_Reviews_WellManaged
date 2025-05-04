from django.contrib.auth.models import User
from .models import Profile
from django.forms.models import ModelForm
from django.forms.widgets import FileInput
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__' # Fields that can be updated
        exclude = ['user']
        widgets = {
            'Image': FileInput(),  # Accept only image files
        }

