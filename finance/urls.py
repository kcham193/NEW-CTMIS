from django.urls import path
from .views import ExpenditureView, RevenueView, ReceiptView, MemberContributionListView,ContributionCreateView



urlpatterns = [
    path('contributions/add/', ContributionCreateView.as_view(), name='contribution-add'), 
    path('contributions/', MemberContributionListView.as_view(), name='member_contributions'),
    path('expenditure/', ExpenditureView.as_view(), name='expenditure'),
    path('revenue/', RevenueView.as_view(), name='revenue'),
    path('receipt/', ReceiptView.as_view(), name='receipt'),
]
