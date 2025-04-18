from django import forms
from django.contrib.auth.models import User


class SimplePasswordChangeForm(forms.Form):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}),
        label="New Password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}),
        label="Confirm Password"
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data



from database.models import Member, Course, Material
class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class MaterialCreateForm(forms.ModelForm):
    class Meta:
        model = Material
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