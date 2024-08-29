from django import forms
from database.models import Material


class MaterialCreateForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'


class MaterialDetailForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'




