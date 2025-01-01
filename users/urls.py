from django.urls import path
from .views import StudentRegisterView, TeacherRegisterView, StudentLoginView, TeacherLoginView

urlpatterns = [
    path('register/student/', StudentRegisterView.as_view(), name='student-register'),
    path('register/teacher/', TeacherRegisterView.as_view(), name='teacher-register'),
    path('login/student/', StudentLoginView.as_view(), name='student-login'),
    path('login/teacher/', TeacherLoginView.as_view(), name='teacher-login'),
]
