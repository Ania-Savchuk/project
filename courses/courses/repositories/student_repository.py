from typing import List, Optional
from courses.courses.models import Student, Registration
from courses.courses.repositories.base_repository import AbstractRepository


class StudentRepository(AbstractRepository):
    def get_all(self) -> List[Student]:

        return list(Student.objects.all())

    def get_by_id(self, student_id: int) -> Optional[Student]:

        try:
            return Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return None

    def create(self, first_name: str, last_name: str, phone_number: str, email: str, registration_date: str, registration: 'Registration') -> Student:
        registration = Registration.objects.get(id=registration)
        student = Student(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            registration_date=registration_date,
            registration=registration
        )
        student.save()
        return student

    def update(self, student_id: int, first_name: str, last_name: str, phone_number: str, email: str, registration_date: str, registration: 'Registration') -> Optional[Student]:

        try:
            student = Student.objects.get(id=student_id)
            student.first_name = first_name
            student.last_name = last_name
            student.phone_number = phone_number
            student.email = email
            student.registration_date = registration_date
            registration = Registration.objects.get(id=registration)
            student.registration = registration
            student.save()
            return student
        except Student.DoesNotExist:
            return None

    def delete(self, student_id: int) -> bool:

        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return True
        except Student.DoesNotExist:
            return False
