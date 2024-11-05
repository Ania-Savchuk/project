from typing import List, Optional
from courses.courses.models import Material, Course
from courses.courses.repositories.base_repository import AbstractRepository


class MaterialRepository(AbstractRepository):
    def get_all(self) -> List[Material]:

        return list(Material.objects.all())

    def get_by_id(self, material_id: int) -> Optional[Material]:

        try:
            return Material.objects.get(id=material_id)
        except Material.DoesNotExist:
            return None

    def create(self, course: Optional[Course], file_path: str, description: Optional[str]) -> Material:
        course = Course.objects.get(id=course)
        material = Material(course=course, file_path=file_path, description=description)
        material.save()
        return material

    def update(self, material_id: int, course: Optional[Course], file_path: str, description: Optional[str]) -> Optional[Material]:

        try:
            material = Material.objects.get(id=material_id)
            course = Course.objects.get(id=course)
            material.course = course
            material.file_path = file_path
            material.description = description
            material.save()
            return material
        except Material.DoesNotExist:
            return None

    def delete(self, material_id: int) -> bool:

        try:
            material = Material.objects.get(id=material_id)
            material.delete()
            return True
        except Material.DoesNotExist:
            return False
