from django import forms

class AttendCheckForm(forms.Form):
    attend = forms.BooleanField(required=True)