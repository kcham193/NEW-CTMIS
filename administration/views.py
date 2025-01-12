from django.views.generic import ListView, DetailView, DeleteView
from database.models import Course, Material, Module
from administration.forms import CourseCreateForm, MaterialCreateForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from database.models import Member
from .forms import MemberCreateForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from templates.administration.utils import send_member_email
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SimplePasswordChangeForm
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse

def verify_account(request, member_id):
    member = Member.objects.get(pk=member_id)
    member.is_verified = True  # Assuming you have an `is_verified` field
    member.save()
    return HttpResponse("Your account has been verified successfully!")


def send_verification_email(request, member_id):
    # Fetch the member object using member_id
    member = Member.objects.get(pk=member_id)
    verification_link = request.build_absolute_uri(reverse('verify_account', args=[member_id]))

    subject = "Account Verification"
    message = f"Hi {member.first_name},\n\nPlease verify your account using the link below:\n{verification_link}\n\nThank you!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [member.email]

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Verification email sent.")


# @login_required
# def member_profile(request):
#     # Fetch the Member object for the logged-in user
#     member = Member.objects.filter(user=request.user).first()
    
#     context = {
#         'member': member,
#     }
    
#     return render(request, 'administration/member.html', context)


class CourseView(LoginRequiredMixin, ListView):
    template_name = 'administration/course.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administration'] = 'active'
        context['course'] = 'active'
        context['module_title'] = 'ADMINISTRATION'
        context['page_title'] = 'COURSE'
        context['course_form'] = CourseCreateForm()
        return context

class CourseDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Course
    template_name = 'administration/course_detail_form.html'
    context_object_name = 'course'

    #def get_queryset(self):
        #return Material.objects.filter(category__iexact='Lecture Notes')  # Case insensitive comparison


class CourseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'administration/course_create_form.html'
    form_class = CourseCreateForm
    success_url = reverse_lazy('course')
    success_message = 'Course created successfully'


class CourseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'administration/course_update_form.html'
    form_class = CourseCreateForm
    success_url = reverse_lazy('course')
    model = Course
    success_message = 'course updated successfully'


class CourseDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Course
    template_name = 'administration/course_delete_form.html'
    success_url = reverse_lazy('course')
    success_message = 'Course deleted successfully'

class ModuleListView(LoginRequiredMixin, ListView):
    template_name = 'administration/module.html'
    model = Module
    context_object_name = 'modules'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administration'] = 'active'
        context['module'] = 'active'
        context['module_title'] = 'ADMINISTRATION'
        context['page_title'] = 'MODULES'
        return context


class ModuleDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Module
    template_name = 'administration/module_detail_form.html'
    context_object_name = 'module'


class ModuleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'administration/module_create_form.html'
    model = Module
    fields = ['name', 'semester', 'course', 'year']
    success_url = reverse_lazy('module')
    success_message = 'Module created successfully'


class ModuleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'administration/module_update_form.html'
    model = Module
    fields = ['name', 'semester', 'course', 'year']
    success_url = reverse_lazy('module')
    success_message = 'Module updated successfully'


class ModuleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Module
    template_name = 'administration/module_delete_form.html'
    success_url = reverse_lazy('module')
    success_message = 'Module deleted successfully'


    
class MaterialView(LoginRequiredMixin, ListView):
    template_name = 'administration/material.html'
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administration'] = 'active'
        context['material'] = 'active'
        context['module_title'] = 'ADMINISTRATION'
        context['page_title'] = 'MATERIAL'
        context['material_form'] = MaterialCreateForm()
        return context

class MaterialDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Material
    template_name = 'administration/material_detail_form.html'
    context_object_name = 'material'

    #def get_queryset(self):
        #return Material.objects.filter(category__iexact='Lecture Notes')  # Case insensitive comparison


class MaterialCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'administration/material_create_form.html'
    form_class = MaterialCreateForm
    success_url = reverse_lazy('material')
    success_message = 'Material created successfully'


class MaterialUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'administration/material_update_form.html'
    form_class = MaterialCreateForm
    success_url = reverse_lazy('material')
    model = Course
    success_message = 'material updated successfully'


class MaterialDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Material
    template_name = 'administration/material_delete_form.html'
    success_url = reverse_lazy('material')
    success_message = 'Material deleted successfully'
    
class MemberView(LoginRequiredMixin, ListView):
    template_name = 'administration/member.html'
    model = Member
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administration'] = 'active'
        context['member'] = 'active'
        context['module_title'] = 'ADMINISTRATION'
        context['page_title'] = 'MEMBERS'
        context['member_form'] = MemberCreateForm()
        return context

class MemberDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Member
    template_name = 'administration/member_detail_form.html'
    context_object_name = 'member'

    #def get_queryset(self):
        #return Material.objects.filter(category__iexact='Lecture Notes')  # Case insensitive comparison


class MemberCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'administration/member_create_form.html'
    form_class = MemberCreateForm
    success_url = reverse_lazy('member')
    success_message = 'Member created successfully'
    
    def form_valid(self, form):
        # First, create the user
        user = User.objects.create_user(
            username=form.cleaned_data['first_name'],  # Assuming you're using email as username
            password=form.cleaned_data['password']  # Password from the form
        )
        
        # Now, save the member form but don't commit yet
        member = form.save(commit=False)
        
        # Assign the created user to the member
        member.user = user
        
        # Now, save the member instance
        member.save()

        # Log in the new user
        # login(self.request, user)
        
        return super().form_valid(form)




class MemberUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'administration/member_update_form.html'
    form_class = MemberCreateForm
    success_url = reverse_lazy('member')
    model = Member
    success_message = 'Member updated successfully'

    def form_valid(self, form):
        # Update member information
        member = form.save(commit=False)

        # If the member is linked to a user, update the user
        if member.user:
            user = member.user
            user.username = form.cleaned_data['first_name']  # Update username
            if form.cleaned_data['password']:  # If a new password is provided
                user.password = make_password(form.cleaned_data['password'])
            user.save()

        member.save()

        return super().form_valid(form)


class MemberDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Member
    template_name = 'administration/member_delete_form.html'
    success_url = reverse_lazy('member')
    success_message = 'Member deleted successfully'



def simple_password_change(request):
    if request.method == 'POST':
        form = SimplePasswordChangeForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']

            # Update the user's password
            user = request.user
            user.password = make_password(new_password)
            user.save()

            messages.success(request, "Your password has been changed successfully.")
            return redirect('login')  # Redirect to the login page or any other page
    else:
        form = SimplePasswordChangeForm()

    return render(request, 'registration/password_change_form.html', {'form': form})
