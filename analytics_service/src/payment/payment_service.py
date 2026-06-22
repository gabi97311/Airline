from .payment_repo import PaymenyRepo

class PaymenytService:
    def __init__(self, payment_repo:PaymenyRepo):
        self.repo = payment_repo
        