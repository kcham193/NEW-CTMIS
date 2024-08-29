from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    

