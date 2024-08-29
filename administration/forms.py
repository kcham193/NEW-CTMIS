from django import forms

from database.models import Member, Course
class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'