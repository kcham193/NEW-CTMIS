from django.urls import path
from .views import ExpenditureView, RevenueView, ReceiptView


urlpatterns = [
    path('expenditure/', ExpenditureView.as_view(), name='expenditure'),
    path('revenue/', RevenueView.as_view(), name='revenue'),
    path('receipt/', ReceiptView.as_view(), name='receipt'),
]
