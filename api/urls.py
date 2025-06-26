from django.urls import path
from accounts.views import RegisterView, LoginView, ProfileView
from courses.views import (
    CourseListView,
    CourseDetailView,
    LessonListView,
    EnrollmentView,
    UserEnrollmentsView,
    CourseManageView,
    LessonDetailView,
    AssignmentCreateView,
    LessonAssignmentsView,
)

app_name = 'api'  # ← обязательно для работы namespace

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Courses
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/manage/', CourseManageView.as_view(), name='course-manage'),
    path('courses/<int:course_id>/lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),

    # Enrollments
    path('enroll/', EnrollmentView.as_view(), name='enroll'),
    path('my-courses/', UserEnrollmentsView.as_view(), name='user-enrollments'),

    # Assignments
    path('lessons/<int:lesson_id>/assignments/', LessonAssignmentsView.as_view(), name='lesson-assignments'),
    path('assignments/submit/', AssignmentCreateView.as_view(), name='assignment-submit'),
]
