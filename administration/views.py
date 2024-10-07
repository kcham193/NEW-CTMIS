from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from database.models import Member, Course
from administration.forms import MemberCreateForm, CourseCreateForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from database.models import Member
from .forms import MemberCreateForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404



from django.contrib.auth.decorators import login_required


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

    
class MaterialView(LoginRequiredMixin, TemplateView):
    template_name = 'administration/material.html'
    
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

