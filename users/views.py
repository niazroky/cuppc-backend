from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer, StudentLoginSerializer, TeacherLoginSerializer


class StudentRegisterView(generics.CreateAPIView):
    """
    View for registering new students.

    Inherits from Django REST framework's `CreateAPIView`, which handles the
    creation of new student users.

    Serializer:
        - Uses `StudentSerializer` to validate and create students.
    """
    serializer_class = StudentSerializer


class TeacherRegisterView(generics.CreateAPIView):
    """
    View for registering new teachers.

    Inherits from Django REST framework's `CreateAPIView`, which handles the
    creation of new teacher users.

    Serializer:
        - Uses `TeacherSerializer` to validate and create teachers.
    """
    serializer_class = TeacherSerializer


class StudentLoginView(generics.GenericAPIView):
    """
    View for student login and token generation.

    Handles login for students using their `varsity_id` and password. On successful
    authentication, it generates and returns a pair of JWT tokens (refresh and access).

    Methods:
        - post: Accepts POST requests for login, validates the student's credentials,
          and issues JWT tokens upon success.

    Serializer:
        - Uses `StudentLoginSerializer` to validate the input data.
    
    Responses:
        - On success: Returns a response containing refresh and access tokens.
        - On failure: Returns an HTTP 401 Unauthorized response with an error message.
    """
    serializer_class = StudentLoginSerializer

    def post(self, request):
        """
        Handles POST requests for student login.

        Validates the input credentials (varsity_id and password), and if valid, generates
        JWT tokens for the student.

        Args:
            request: The HTTP request containing login data.

        Returns:
            Response: A JSON response containing the JWT tokens if login is successful, 
                      or an error message if authentication fails.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        varsity_id = serializer.validated_data['varsity_id']
        password = serializer.validated_data['password']

        try:
            user = Student.objects.get(varsity_id=varsity_id)
        except Student.DoesNotExist:
            return Response({'detail': 'Invalid Varsity ID or password'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'detail': 'Invalid Varsity ID or password'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class TeacherLoginView(generics.GenericAPIView):
    """
    View for teacher login and token generation.

    Handles login for teachers using their `email` and password. On successful
    authentication, it generates and returns a pair of JWT tokens (refresh and access).

    Methods:
        - post: Accepts POST requests for login, validates the teacher's credentials,
          and issues JWT tokens upon success.

    Serializer:
        - Uses `TeacherLoginSerializer` to validate the input data.
    
    Responses:
        - On success: Returns a response containing refresh and access tokens.
        - On failure: Returns an HTTP 401 Unauthorized response with an error message.
    """
    serializer_class = TeacherLoginSerializer

    def post(self, request):
        """
        Handles POST requests for teacher login.

        Validates the input credentials (email and password), and if valid, generates
        JWT tokens for the teacher.

        Args:
            request: The HTTP request containing login data.

        Returns:
            Response: A JSON response containing the JWT tokens if login is successful, 
                      or an error message if authentication fails.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = Teacher.objects.get(email=email)
        except Teacher.DoesNotExist:
            return Response({'detail': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'detail': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })