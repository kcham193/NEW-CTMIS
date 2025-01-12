from django import forms
from database.models import Contribution, Receipt, Voucher

class ReceiptForm(forms.ModelForm):
    contribution = forms.ModelChoiceField(queryset=Contribution.objects.none(), label="Select Contribution")

    class Meta:
        model = Receipt
        fields = ['contribution', 'recorder_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter out contributions that already have a receipt
        self.fields['contribution'].queryset = Contribution.objects.exclude(
            id__in=Receipt.objects.values_list('contribution_id', flat=True)
        )

    def clean(self):
        cleaned_data = super().clean()
        contribution = cleaned_data.get('contribution')

        # Ensure a receipt does not already exist for the selected contribution
        if contribution and Receipt.objects.filter(contribution=contribution).exists():
            raise forms.ValidationError("A receipt for this contribution already exists.")
        return cleaned_data


class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = ['voucher_code', 'amount', 'description', 'Approved_by']
