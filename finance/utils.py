from finance.models import Receipt
from database.models import Contribution

def generate_receipts():
    contributions = Contribution.objects.filter(receipt__isnull=True)
    for contribution in contributions:
        Receipt.objects.create(
            contribution=contribution,
            receipt_number=f"RCPT-{contribution.id}"
        )
