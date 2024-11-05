from django.db import transaction
from courses.courses.repositories.course_level_repository import CoursLevelRepository
from courses.courses.repositories.course_repository import CourseRepository
from courses.courses.repositories.group_repository import GroupRepository
from courses.courses.repositories.instructor_repository import InstructorRepository
from courses.courses.repositories.mark_repository import MarkRepository
from courses.courses.repositories.material_repository import MaterialRepository
from courses.courses.repositories.payment_repository import PaymentRepository
from courses.courses.repositories.registration_repository import RegistrationRepository
from courses.courses.repositories.schedule_repository import ScheduleRepository
from courses.courses.repositories.student_course_repository import StudentCourseRepository
from courses.courses.repositories.student_repository import StudentRepository


class ComputerCourseContext:
    def __init__(self):
        self.course_repository = CourseRepository()
        self.student_repository = StudentRepository()
        self.instructor_repository = InstructorRepository()
        self.mark_repository = MarkRepository()
        self.material_repository = MaterialRepository()
        self.payment_repository = PaymentRepository()
        self.registration_repository = RegistrationRepository()
        self.schedule_repository = ScheduleRepository()
        self.student_course_repository = StudentCourseRepository()
        self.group_repository = GroupRepository()
        self.course_level_repository = CoursLevelRepository()

    def __enter__(self):

        self._transaction = transaction.atomic()
        self._transaction.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type is not None:
            # Rollback if there was an exception
            self.rollback()
        else:
            # Commit if everything went smoothly
            self.commit()

    def commit(self):

        try:
            self._transaction.__exit__(None, None, None)
        except Exception as e:
            print(f"Failed to commit transaction: {e}")
            raise

    def rollback(self):

        try:
            self._transaction.__exit__(Exception, Exception(), None)
        except Exception as e:
            print(f"Failed to rollback transaction: {e}")
            raise
