from django.urls import path
from .views import HomeView ,FeeCreateView, FeeListView ,FeeDeleteView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('feestructure/create', FeeCreateView.as_view(), name='create_fee'),
    path('feestructure/detail/<str:pk>', FeeListView.as_view(), name='feestructure'),
    path('feestructure/delete/<str:pk>', FeeDeleteView.as_view(), name='delete_fee')
]
