from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.forms import  FeeCreateForm
from database.models import  FeeStructure, FeeSummary,Contribution
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

@method_decorator(never_cache, name='dispatch')
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    context_object_name = 'contributions'
    
    def get_queryset(self):
        # Return only the contributions made by the logged-in member
        return Contribution.objects.filter(member__user=self.request.user)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the contributions made by the logged-in member
        contributions = self.get_queryset()
        
        # Calculate the total amount paid by the logged-in member
        total_paid = contributions.aggregate(Sum('amount'))['amount__sum'] or 0
        
        # Fetch the total amount the member is supposed to pay from the FeeStructure
        total_payable = FeeStructure.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        
        # Calculate the percentage paid
        percentage_paid = (total_paid / total_payable) * 100 if total_payable > 0 else 0
        
        # Add the calculated values to the context
        context['total_paid'] = total_paid
        context['total_payable'] = total_payable
        context['percentage_paid'] = percentage_paid
        
        context['academic'] = 'active'
        context['feestructure'] = 'active'
        context['module_title'] = 'DASHBOARD'
        context['page_title'] = 'HOME'
        context['fee_list'] = FeeStructure.objects.all()  # Fetch fee structures
        context['fee_form'] = FeeCreateForm()
        return context
        
class FeeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'dashboard/fee_create_form.html'
    model = FeeStructure
    form_class = FeeCreateForm
    success_url = reverse_lazy('home')
    success_message = 'fee created successfully'
    
from django.db.models import Sum

class FeeListView(LoginRequiredMixin, ListView):
    model = FeeStructure
    template_name = 'dashboard/index.html'
    context_object_name = 'feestructure'

    # def get_queryset(self):
    #     # Get the full fee structure list
    #     return FeeStructure.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     # Fetch the contributions made by the logged-in member
    #     contributions = self.get_queryset()
        
    #     # Calculate the total amount paid by the logged-in member
    #     total_paid = contributions.aggregate(Sum('amount'))['amount__sum'] or 0
        
    #     # Fetch the total amount the member is supposed to pay from the FeeStructure
    #     total_payable = FeeStructure.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        
    #     # Calculate the percentage paid
    #     percentage_paid = (total_paid / total_payable) * 100 if total_payable > 0 else 0
        
    #     # Add the fee list and calculated values to the context
    #     context['fee_list'] = self.get_queryset()
    #     context['total_paid'] = total_paid
    #     context['total_payable'] = total_payable
    #     context['percentage_paid'] = percentage_paid
    #     context['academic'] = 'active'
    #     context['feestructure'] = 'active'
    #     context['module_title'] = ''
    #     context['page_title'] = 'DASHBOARD'
        
    #     return context



    
class FeeDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'dashboard/fee_delete_form.html'
    model = FeeStructure
    success_url = reverse_lazy('home')
    success_message = 'fee deleted successfully'