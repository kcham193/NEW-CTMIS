from django import forms
from django.contrib.auth.models import User


from database.models import Member, Course
class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'



class MemberCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)  # Allow blank if updating

    class Meta:
        model = Member
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'physical_address', 'place_of_domicile', 'current_place_of_residency', 'year_of_study', 'course', 'ministry', 'current_place_of_worship', 'previous_place_of_worship', 'next_of_kin', 'image', 'sex', 'role']
        exclude = ['user']  # The user is handled in the view, not directly in the form

password = forms.CharField(widget=forms.PasswordInput)

def save(self, commit=True):
        member = super().save(commit=False)
        
        # Create the user object here
        user = User(
            username=member.first_name,  # or any other field as username
            email=member.email,
            is_active=True
        )
        user.set_password(self.cleaned_data['password'])  # Hashing the password
        
        if commit:
            user.save()
            member.user = user  # Associate the member with the user
            member.save()
        
        return member