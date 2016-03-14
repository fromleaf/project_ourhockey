from django import forms

class AttendCheckForm(forms.Form):
    attend = forms.BooleanField(required=True)
    
    
class InsertPlayerForm(forms.Form):
    name = forms.CharField(max_length=200)
    birthday = forms.DateField()
    gender_choices = (('1', 'Male'), ('2', 'Female'))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender_choices)
    
    """
    if birthday is over 19 years
        adult_checked == true
    is it possible to automatically checked block after input the birthday value? 
    """
    adult = forms.CheckboxInput()
    back_number = forms.IntegerField()
    duty = forms.RadioSelect()
    position = forms.RadioSelect()
    profile_image = forms.ImageField()