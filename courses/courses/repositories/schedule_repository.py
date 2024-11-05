from typing import List, Optional
from courses.courses.models import Schedule, Course, Group
from courses.courses.repositories.base_repository import AbstractRepository


class ScheduleRepository(AbstractRepository):
    def get_all(self) -> List[Schedule]:

        return list(Schedule.objects.all())

    def get_by_id(self, schedule_id: int) -> Optional[Schedule]:

        try:
            return Schedule.objects.get(id=schedule_id)
        except Schedule.DoesNotExist:
            return None

    def create(self, course: 'Course', group: 'Group', session_date: str, duration_hours: int) -> Schedule:
        group = Group.objects.get(id=group)
        course = Course.objects.get(id=course)
        schedule = Schedule(course=course, group=group, session_date=session_date, duration_hours=duration_hours)
        schedule.save()
        return schedule

    def update(self, schedule_id: int, course: 'Course', group: 'Group', session_date: str, duration_hours: int) -> Optional[Schedule]:

        try:
            schedule = Schedule.objects.get(id=schedule_id)
            course = Course.objects.get(id=course)
            schedule.course = course
            group = Group.objects.get(id=group)
            schedule.group = group
            schedule.session_date = session_date
            schedule.duration_hours = duration_hours
            schedule.save()
            return schedule
        except Schedule.DoesNotExist:
            return None

    def delete(self, schedule_id: int) -> bool:

        try:
            schedule = Schedule.objects.get(id=schedule_id)
            schedule.delete()
            return True
        except Schedule.DoesNotExist:
            return False
