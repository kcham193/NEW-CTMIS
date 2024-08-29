from django import forms
from .models import Material, Course

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('name','file')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_code' , 'name')