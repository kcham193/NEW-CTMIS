from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from database.models import Contribution, Member,FeeStructure
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.
class ExpenditureView(LoginRequiredMixin, TemplateView):
    template_name = 'finance/expenditure.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finance'] = 'active'
        context['expenditure'] = 'active'
        
    
class RevenueView(LoginRequiredMixin, TemplateView):
    template_name = 'finance/revenue.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finance'] = 'active'
        context['revenue'] = 'active'
        
class ReceiptView(LoginRequiredMixin, TemplateView):
    template_name = 'finance/receipt.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finance'] = 'active'
        context['receipt'] = 'active'
    





from django.db.models import Sum

class MemberContributionListView(LoginRequiredMixin, ListView):
    model = Contribution
    template_name = 'finance/member_contributions.html'
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
        
        return context




class ContributionCreateView(LoginRequiredMixin, CreateView):
    model = Contribution
    fields = ['member', 'name', 'description', 'amount']
    template_name = 'finance/contribution_form.html'
    success_url = reverse_lazy('contribution-add')  # Redirect to a contribution list or another page

    
