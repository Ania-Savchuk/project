from typing import List, Optional

from courses.courses.models import Mark, Student
from courses.courses.repositories.base_repository import AbstractRepository


class MarkRepository(AbstractRepository):
    def get_all(self) -> List[Mark]:

        return list(Mark.objects.all())

    def get_by_id(self, mark_id: int) -> Optional[Mark]:

        try:
            return Mark.objects.get(id=mark_id)
        except Mark.DoesNotExist:
            return None

    def create(self, mark: float, date_mark: str, comment: Optional[str], student: Optional['Student']) -> Mark:
        student = Student.objects.get(id=student)
        mark_instance = Mark(mark=mark, date_mark=date_mark, comment=comment, student=student)
        mark_instance.save()
        return mark_instance

    def update(self, mark_id: int, mark: float, date_mark: str, comment: Optional[str], student: Optional['Student']) -> Optional[Mark]:

        try:
            mark_instance = Mark.objects.get(id=mark_id)
            mark_instance.mark = mark
            mark_instance.date_mark = date_mark
            mark_instance.comment = comment
            student = Student.objects.get(id=student)
            mark_instance.student = student
            mark_instance.save()
            return mark_instance
        except Mark.DoesNotExist:
            return None

    def delete(self, mark_id: int) -> bool :

        try:
            mark_instance = Mark.objects.get(id=mark_id)
            mark_instance.delete()
            return True
        except Mark.DoesNotExist:
            return False
