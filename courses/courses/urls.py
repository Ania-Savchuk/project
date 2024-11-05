"""courses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import (
    CoursLevelViewSet, CourseViewSet, GroupViewSet, InstructorViewSet, MarkViewSet, MaterialViewSet,
    PaymentViewSet, RegistrationViewSet, ScheduleViewSet, StudentViewSet, StudentCourseViewSet
)

router = DefaultRouter()
router.register(r'course-levels', CoursLevelViewSet, basename='course-level')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'instructors', InstructorViewSet, basename='instructor')
router.register(r'marks', MarkViewSet, basename='mark')
router.register(r'materials', MaterialViewSet, basename='material')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'registrations', RegistrationViewSet, basename='registration')
router.register(r'schedules', ScheduleViewSet, basename='schedule')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'student-courses', StudentCourseViewSet, basename='student-course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]


