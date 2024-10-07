from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from database.models import Material, Member, FeeStructure, FeeSummary
from academic.forms import MaterialCreateForm

# Update to your template file

    


class LectureNotesView(LoginRequiredMixin, ListView):
    template_name = 'academic/lecture_notes.html'
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['academic'] = 'active'
        context['lecture_notes'] = 'active'
        context['module_title'] = 'ACADEMICS'
        context['page_title'] = 'LECTURE NOTES'
        context['material_form'] = MaterialCreateForm()
        return context

    def get_queryset(self):
        return Material.objects.filter(category='Lecture Notes')

class MaterialDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Material
    template_name = 'academic/material_detail_form.html'
    context_object_name = 'material'

class MaterialCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'academic/material_create_form.html'
    form_class = MaterialCreateForm
    success_url = reverse_lazy('lecture_notes')
    success_message = 'Material created successfully'

class MaterialUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'academic/material_update_form.html'
    form_class = MaterialCreateForm
    success_url = reverse_lazy('lecture_notes')  # Ensure this is pointing to 'lecture_notes'
    model = Material
    success_message = 'Material updated successfully'

class MaterialDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'academic/material_delete._form.html'  # Ensure the template name is correct
    model = Material
    success_url = reverse_lazy('lecture_notes')  # Ensure this is pointing to 'lecture_notes'
    success_message = 'Material deleted successfully'

class AssignmentView(LoginRequiredMixin, ListView):
    template_name = 'academic/assignment.html'
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['academic'] = 'active'
        context['assignment'] = 'active'
        context['module_title'] = 'ACADEMICS'
        context['page_title'] = 'ASSIGNMENTS'
        return context

    def get_queryset(self):
        return Material.objects.filter(category='Assignments')

class AssignmentMaterialUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'academic/material_update_form.html'
    form_class = MaterialCreateForm
    success_url = reverse_lazy('assignments')  # Ensure this is pointing to 'assignments'
    model = Material
    success_message = 'Material updated successfully'

class AssignmentMaterialDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'academic/material_delete._form.html'
    model = Material
    success_url = reverse_lazy('assignments')  # Ensure this is pointing to 'assignments'
    success_message = 'Material deleted successfully'

class ReferenceMaterialView(LoginRequiredMixin, ListView):
    template_name = 'academic/reference_material.html'
    model = Material

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['academic'] = 'active'
        context['reference_materials'] = 'active'
        context['module_title'] = 'ACADEMICS'
        context['page_title'] = 'REFERENCE MATERIALS'
        return context

    def get_queryset(self):
        return Material.objects.filter(category='Reference Materials')

class ReferenceMaterialUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'academic/material_update_form.html'
    form_class = MaterialCreateForm
    success_url = reverse_lazy('reference_materials')  # Ensure this is pointing to 'reference_materials'
    model = Material
    success_message = 'Material updated successfully'

class ReferenceMaterialDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'academic/material_delete._form.html'
    model = Material
    success_url = reverse_lazy('reference_materials')  # Ensure this is pointing to 'reference_materials'
    success_message = 'Material deleted successfully'

