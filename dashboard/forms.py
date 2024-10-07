from django import forms
from database.models import  FeeStructure



class FeeCreateForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = '__all__'






