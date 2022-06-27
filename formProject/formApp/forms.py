from django import forms
from django.core import validators

class formName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label='Enter your email again:')
    text = forms.CharField( widget = forms.Textarea )
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data=super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verifyEmail']
        if email != vmail:
            raise forms.ValidationError("Your Email doesnt match you dumbass")
