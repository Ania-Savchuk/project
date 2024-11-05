from typing import List, Optional
from courses.courses.models import Instructor
from courses.courses.repositories.base_repository import AbstractRepository


class InstructorRepository(AbstractRepository):
    def get_all(self) -> List[Instructor]:

        return list(Instructor.objects.all())

    def get_by_id(self, instructor_id: int) -> Optional[Instructor]:

        try:
            return Instructor.objects.get(id=instructor_id)
        except Instructor.DoesNotExist:
            return None

    def create(self, first_name: str, last_name: str, specialization: Optional[str] = None) -> Instructor:

        instructor = Instructor(first_name=first_name, last_name=last_name, specialization=specialization)
        instructor.save()
        return instructor

    def update(self, instructor_id: int, first_name: str, last_name: str, specialization: Optional[str] = None) -> Optional[Instructor]:

        try:
            instructor = Instructor.objects.get(id=instructor_id)
            instructor.first_name = first_name
            instructor.last_name = last_name
            instructor.specialization = specialization
            instructor.save()
            return instructor
        except Instructor.DoesNotExist:
            return None

    def delete(self, instructor_id: int) -> bool:

        try:
            instructor = Instructor.objects.get(id=instructor_id)
            instructor.delete()
            return True
        except Instructor.DoesNotExist:
            return False
