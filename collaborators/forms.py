from django.forms.models import ModelForm
from django import forms
from collaborators.models import Collaborator
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',]

class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ['entity','is_ibmer',]