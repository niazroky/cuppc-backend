from rest_framework import serializers
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Student` model.
    
    This serializer handles the conversion of `Student` model instances to JSON format
    and vice versa. It ensures that the password field is write-only for security reasons.

    Fields:
        - full_name: The full name of the student.
        - varsity_id: The unique identifier for students.
        - email: The student's email address.
        - password: The student's hashed password (write-only).
    
    Methods:
        - create: Overrides the create method to ensure that the password is hashed
          when creating a new `Student` instance using the custom user manager.
    """
    class Meta:
        model = Student
        fields = ['full_name', 'varsity_id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Prevent password from being returned in responses

    def create(self, validated_data):
        """
        Creates a new `Student` instance with hashed password.
        
        Args:
            validated_data (dict): The validated data for creating a student.
        
        Returns:
            Student: The created `Student` instance.
        """
        user = Student.objects.create_user(**validated_data)
        return user


class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer for the `Teacher` model.
    
    This serializer handles the conversion of `Teacher` model instances to JSON format
    and vice versa. It ensures that the password field is write-only for security reasons.

    Fields:
        - full_name: The full name of the teacher.
        - email: The unique email of the teacher (validated to end with '@physics.cu.ac.bd').
        - password: The teacher's hashed password (write-only).
    
    Methods:
        - create: Overrides the create method to ensure that the password is hashed
          when creating a new `Teacher` instance using the custom user manager.
    """
    class Meta:
        model = Teacher
        fields = ['full_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Prevent password from being returned in responses

    def create(self, validated_data):
        """
        Creates a new `Teacher` instance with hashed password.
        
        Args:
            validated_data (dict): The validated data for creating a teacher.
        
        Returns:
            Teacher: The created `Teacher` instance.
        """
        user = Teacher.objects.create_user(**validated_data)
        return user


class StudentLoginSerializer(serializers.Serializer):
    """
    Serializer for handling student login.

    Fields:
        - varsity_id: The unique identifier for students, used for authentication.
        - password: The password of the student.
    """
    varsity_id = serializers.CharField()
    password = serializers.CharField()


class TeacherLoginSerializer(serializers.Serializer):
    """
    Serializer for handling teacher login.

    Fields:
        - email: The email of the teacher, used for authentication.
        - password: The password of the teacher.
    """
    email = serializers.CharField()
    password = serializers.CharField()