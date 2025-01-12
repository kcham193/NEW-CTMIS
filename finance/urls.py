from django.urls import path
from .views import ExpenditureView, ReceiptView, MemberContributionListView,ContributionCreateView,ReceiptListView, ReceiptCreateView, VoucherListView, VoucherCreateView



urlpatterns = [
    path('contributions/add/', ContributionCreateView.as_view(), name='contribution-add'), 
    path('contributions/', MemberContributionListView.as_view(), name='member_contributions'),
    path('expenditure/', ExpenditureView.as_view(), name='expenditure'),
    path('receipt/', ReceiptView.as_view(), name='receipt'),
    path('receipts/', ReceiptListView.as_view(), name='receipt_list'),
    path('receipts/new/', ReceiptCreateView.as_view(), name='create_receipt'),
    path('vouchers/', VoucherListView.as_view(), name='voucher_list'),
    path('vouchers/new/', VoucherCreateView.as_view(), name='voucher_create'),
]

