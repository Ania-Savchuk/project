from typing import Optional, List
from courses.courses.models import CoursLevel
from courses.courses.repositories.base_repository import AbstractRepository


class CoursLevelRepository(AbstractRepository):
    def get_all(self) -> List[CoursLevel]:
        return list(CoursLevel.objects.all())

    def get_by_id(self, level_id: int) -> Optional[CoursLevel]:
        try:
            return CoursLevel.objects.get(id=level_id)
        except CoursLevel.DoesNotExist:
            return None

    def create(self, level_name: str, description: Optional[str] = None) -> CoursLevel:
        level = CoursLevel(level_name=level_name, description=description)
        level.save()
        return level

    def update(self, level_id: int, level_name: str, description: Optional[str] = None) -> Optional[CoursLevel]:
        try:
            level = CoursLevel.objects.get(id=level_id)
            level.level_name = level_name
            level.description = description
            level.save()
            return level
        except CoursLevel.DoesNotExist:
            return None

    def delete(self, level_id: int) -> bool:
        try:
            level = CoursLevel.objects.get(id=level_id)
            level.delete()
            return True
        except CoursLevel.DoesNotExist:
            return False
