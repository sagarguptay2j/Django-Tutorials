from django import forms
from testApp.models import Users

class formName(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'
