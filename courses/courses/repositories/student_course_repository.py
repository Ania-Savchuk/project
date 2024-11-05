from typing import Optional, List
from courses.courses.models import StudentCourse, Course, Student
from courses.courses.repositories.base_repository import AbstractRepository


class StudentCourseRepository(AbstractRepository):
    def get_all(self) -> List[StudentCourse]:
        return list(StudentCourse.objects.all())

    def get_by_id(self, student_id: int) -> Optional[StudentCourse]:

        try:
            return StudentCourse.objects.get(student_id=student_id)
        except StudentCourse.DoesNotExist:
            return None

    def create(self, student: 'Student', course: 'Course') -> StudentCourse:
        course = Course.objects.get(id=course)
        student = Student.objects.get(id=student)
        student_course = StudentCourse(student=student, course=course)
        student_course.save()
        return student_course

    def update(self, student_id: int, course: 'Course') -> Optional[StudentCourse]:

        try:
            student_course = StudentCourse.objects.get(student_id=student_id)
            course = Course.objects.get(id=course)
            student_course.course = course
            student_course.save()
            return student_course
        except StudentCourse.DoesNotExist:
            return None

    def delete(self, student_id: int) -> bool:

        try:
            student_course = StudentCourse.objects.get(student_id=student_id)
            student_course.delete()
            return True
        except StudentCourse.DoesNotExist:
            return False
