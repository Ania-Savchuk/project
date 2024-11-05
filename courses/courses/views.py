from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (
    CoursLevelSerializer, CourseSerializer, GroupSerializer, InstructorSerializer, MarkSerializer,
    MaterialSerializer, PaymentSerializer, RegistrationSerializer, ScheduleSerializer, StudentSerializer,
    StudentCourseSerializer
)
from courses.courses.repositories.computer_courses_context import ComputerCourseContext

class CoursLevelViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                course_levels = uow.course_level_repository.get_all()
                serializer = CoursLevelSerializer(course_levels, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                course_level = uow.course_level_repository.get_by_id(pk)
                if not course_level:
                    raise NotFound("Course level not found.")
                serializer = CoursLevelSerializer(course_level)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Course level not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                course_level = uow.course_level_repository.create(**request.data)
                serializer = CoursLevelSerializer(course_level)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                course_level = uow.course_level_repository.update(pk, **request.data)
                serializer = CoursLevelSerializer(course_level)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Course level not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.course_level_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Course level not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CourseViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                courses = uow.course_repository.get_all()
                serializer = CourseSerializer(courses, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                course = uow.course_repository.get_by_id(pk)
                serializer = CourseSerializer(course)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                course = uow.course_repository.create(**request.data)
                serializer = CourseSerializer(course)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                course = uow.course_repository.update(pk, **request.data)
                serializer = CourseSerializer(course)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.course_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GroupViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                groups = uow.group_repository.get_all()
                serializer = GroupSerializer(groups, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                groups = uow.group_repository.get_by_id(pk)
                serializer = GroupSerializer(groups, many=True)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                groups = uow.group_repository.create(**request.data)
                serializer = GroupSerializer(groups)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                groups = uow.group_repository.update(pk, **request.data)
                serializer = GroupSerializer(groups)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.group_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class InstructorViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                instructors = uow.instructor_repository.get_all()
                serializer = InstructorSerializer(instructors, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                instructor = uow.instructor_repository.get_by_id(pk)
                serializer = InstructorSerializer(instructor)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Instructor not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                instructor = uow.instructor_repository.create(**request.data)
                serializer = InstructorSerializer(instructor)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                instructor = uow.instructor_repository.update(pk, **request.data)
                serializer = InstructorSerializer(instructor)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Instructor not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.instructor_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Instructor not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MarkViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                marks = uow.mark_repository.get_all()
                serializer = MarkSerializer(marks, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                mark = uow.mark_repository.get_by_id(pk)
                serializer = MarkSerializer(mark)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Mark not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                mark = uow.mark_repository.create(**request.data)
                serializer = MarkSerializer(mark)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                mark = uow.mark_repository.update(pk, **request.data)
                serializer = MarkSerializer(mark)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Mark not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.mark_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Mark not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MaterialViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                materials = uow.material_repository.get_all()
                serializer = MaterialSerializer(materials, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                material = uow.material_repository.get_by_id(pk)
                serializer = MaterialSerializer(material)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Material not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                material = uow.material_repository.create(**request.data)
                serializer = MaterialSerializer(material)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                material = uow.material_repository.update(pk, **request.data)
                serializer = MaterialSerializer(material)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Material not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.material_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Material not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ScheduleViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                schedules = uow.schedule_repository.get_all()
                serializer = ScheduleSerializer(schedules, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                schedule = uow.schedule_repository.get_by_id(pk)
                serializer = ScheduleSerializer(schedule)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                schedule = uow.schedule_repository.create(**request.data)
                serializer = ScheduleSerializer(schedule)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                schedule = uow.schedule_repository.update(pk, **request.data)
                serializer = ScheduleSerializer(schedule)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.schedule_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PaymentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                payments = uow.payment_repository.get_all()
                serializer = PaymentSerializer(payments, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                payment = uow.payment_repository.get_by_id(pk)
                serializer = PaymentSerializer(payment)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                payment = uow.payment_repository.create(**request.data)
                serializer = PaymentSerializer(payment)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                payment = uow.payment_repository.update(pk, **request.data)
                serializer = PaymentSerializer(payment)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.payment_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RegistrationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                registrations = uow.registration_repository.get_all()
                serializer = RegistrationSerializer(registrations, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                registrations = uow.registration_repository.get_by_id(pk)
                serializer = RegistrationSerializer(registrations)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Registration not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                registrations = uow.registration_repository.create(**request.data)
                serializer = RegistrationSerializer(registrations)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                registrations = uow.registration_repository.update(pk, **request.data)
                serializer = RegistrationSerializer(registrations)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Registration not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.registration_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Registration not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StudentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                students = uow.student_repository.get_all()
                serializer = StudentSerializer(students, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                student = uow.student_repository.get_by_id(pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                student = uow.student_repository.create(**request.data)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                student = uow.student_repository.update(pk, **request.data)
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.student_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StudentCourseViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        with ComputerCourseContext() as uow:
            try:
                students_courses = uow.student_course_repository.get_all()
                serializer = StudentCourseSerializer(students_courses, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                student_course = uow.student_course_repository.get_by_id(pk)
                serializer = StudentCourseSerializer(student_course)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Student course not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        with ComputerCourseContext() as uow:
            try:
                student_course = uow.student_course_repository.create(**request.data)
                serializer = StudentCourseSerializer(student_course)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                student_course = uow.student_course_repository.update(pk, **request.data)
                serializer = StudentCourseSerializer(student_course)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'error': 'Student course not found'}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        with ComputerCourseContext() as uow:
            try:
                uow.student_course_repository.delete(pk)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except ObjectDoesNotExist:
                return Response({'error': 'Student course not found'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





