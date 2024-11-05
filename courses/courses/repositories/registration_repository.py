from typing import List, Optional
from courses.courses.models import Registration, Course
from courses.courses.repositories.base_repository import AbstractRepository


class RegistrationRepository(AbstractRepository):
    def get_all(self) -> List[Registration]:

        return list(Registration.objects.all())

    def get_by_id(self, registration_id: int) -> Optional[Registration]:

        try:
            return Registration.objects.get(id=registration_id)
        except Registration.DoesNotExist:
            return None

    def create(self, registration_date: str, payment_status: str, course: 'Course') -> Registration:

        course = Course.objects.get(id=course)
        registration = Registration(registration_date=registration_date, payment_status=payment_status, course=course)
        registration.save()
        return registration

    def update(self, registration_id: int, registration_date: str, payment_status: str, course: 'Course') -> Optional[Registration]:

        try:
            registration = Registration.objects.get(id=registration_id)
            registration.registration_date = registration_date
            registration.payment_status = payment_status
            course = Course.objects.get(id=course)
            registration.course = course
            registration.save()
            return registration
        except Registration.DoesNotExist:
            return None

    def delete(self, registration_id: int) -> bool:

        try:
            registration = Registration.objects.get(id=registration_id)
            registration.delete()
            return True
        except Registration.DoesNotExist:
            return False
