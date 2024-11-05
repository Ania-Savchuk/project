from typing import List, Optional
from courses.courses.models import Payment, Registration
from courses.courses.repositories.base_repository import AbstractRepository


class PaymentRepository(AbstractRepository):
    def get_all(self) -> List[Payment]:

        return list(Payment.objects.all())

    def get_by_id(self, payment_id: int) -> Optional[Payment]:

        try:
            return Payment.objects.get(id=payment_id)
        except Payment.DoesNotExist:
            return None

    def create(self, registration: 'Registration', amount: float, payment_date: Optional[str]) -> Payment:

        registration = Registration.objects.get(id=registration)
        payment = Payment(registration=registration, amount=amount, payment_date=payment_date)
        payment.save()
        return payment

    def update(self, payment_id: int, registration: 'Registration', amount: float, payment_date: Optional[str]) -> Optional[Payment]:

        try:
            payment = Payment.objects.get(id=payment_id)
            registration = Registration.objects.get(id=registration)
            payment.registration = registration
            payment.amount = amount
            payment.payment_date = payment_date
            payment.save()
            return payment
        except Payment.DoesNotExist:
            return None

    def delete(self, payment_id: int) -> bool:

        try:
            payment = Payment.objects.get(id=payment_id)
            payment.delete()
            return True
        except Payment.DoesNotExist:
            return False
