from django import forms
from. models import HTMLFile

class HTMLFileForm(forms.ModelForm):
    class Meta:
        model = HTMLFile
        fields = ['file']