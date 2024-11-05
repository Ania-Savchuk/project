from typing import List, Optional
from courses.courses.models import Group, Student, Instructor
from courses.courses.repositories.base_repository import AbstractRepository


class GroupRepository(AbstractRepository):
    def get_all(self) -> List[Group]:
        return list(Group.objects.all())

    def get_by_id(self, group_id: int) -> Optional[Group]:

        try:
            return Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return None

    def create(self, group_name: str, number_of_students: int, instructor: Optional['Instructor'], student: 'Student') -> Group:
        instructor = Instructor.objects.get(id=instructor)
        student = Student.objects.get(id=student)
        group = Group(group_name=group_name, number_of_students=number_of_students, instructor=instructor, student=student)
        group.save()
        return group

    def update(self, group_id: int, group_name: str, number_of_students: int, instructor: Optional['Instructor'], student: 'Student') -> Optional[Group]:

        try:
            group = Group.objects.get(id=group_id)
            group.group_name = group_name
            group.number_of_students = number_of_students
            instructor = Instructor.objects.get(id=instructor)
            group.instructor = instructor
            student = Student.objects.get(id=student)
            group.student = student
            group.save()
            return group
        except Group.DoesNotExist:
            return None

    def delete(self, group_id: int) -> bool:

        try:
            group = Group.objects.get(id=group_id)
            group.delete()
            return True
        except Group.DoesNotExist:
            return False
