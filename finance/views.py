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
        
    
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from database.models import Receipt
from .forms import ReceiptForm

from django.db.models import Sum

class ReceiptListView(ListView):
    model = Receipt
    template_name = 'finance/receipt_list.html'
    context_object_name = 'receipts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_receipts = Receipt.objects.aggregate(total=Sum('amount'))['total'] or 0
        total_vouchers = Voucher.objects.aggregate(total=Sum('amount'))['total'] or 0
        total_available = total_receipts - total_vouchers

        context['total_amount'] = total_receipts
        context['total_available'] = total_available
        return context

class ReceiptCreateView(CreateView):
    model = Receipt
    form_class = ReceiptForm
    template_name = 'finance/receipt_form.html'
    success_url = reverse_lazy('create_receipt')

    def form_valid(self, form):
        # Automatically set the member based on the selected contribution
        contribution = form.cleaned_data['contribution']
        form.instance.member = contribution.member
        receipt = form.save(commit=False)
        receipt.save()

        return super().form_valid(form)


        
class ReceiptView(LoginRequiredMixin, TemplateView):
    template_name = 'finance/receipt.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['finance'] = 'active'
        context['receipt'] = 'active'

from django.db import models
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from database.models import Voucher
from .forms import VoucherForm

class VoucherListView(ListView):
    model = Voucher
    template_name = 'finance/voucher_list.html'
    context_object_name = 'vouchers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_amount'] = Voucher.objects.aggregate(total=models.Sum('amount'))['total'] or 0
        return context

class VoucherCreateView(CreateView):
    model = Voucher
    form_class = VoucherForm
    template_name = 'finance/voucher_form.html'
    success_url = reverse_lazy('voucher_create')

    

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
        context['finance'] = 'active'
        context['contribution'] = 'active'
        context['module_title'] = 'FINANCE'
        context['page_title'] = 'CONTRIBUTIONS'
        
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

    

