from typing import List, Optional
from courses.courses.models import Course, CoursLevel
from courses.courses.repositories.base_repository import AbstractRepository


class CourseRepository(AbstractRepository):
    def get_all(self) -> List[Course]:
        return list(Course.objects.all())

    def get_by_id(self, course_id: int) -> Optional[Course]:

        try:
            return Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return None

    def create(self, name: str, description: Optional[str], duration: int, price: float, level: Optional[CoursLevel]) -> Course:
        level = CoursLevel.objects.get(id=level)
        course = Course(name=name, description=description, duration=duration, price=price, level=level)
        course.save()
        return course

    def update(self, course_id: int, name: str, description: Optional[str], duration: int, price: float, level: Optional[CoursLevel]) -> Optional[Course]:

        try:
            course = Course.objects.get(id=course_id)
            course.name = name
            course.description = description
            course.duration = duration
            course.price = price
            level = CoursLevel.objects.get(id=level)
            course.level = level
            course.save()
            return course
        except Course.DoesNotExist:
            return None

    def delete(self, course_id: int) -> bool:
        try:
            course = Course.objects.get(id=course_id)
            course.delete()
            return True
        except Course.DoesNotExist:
            return False
