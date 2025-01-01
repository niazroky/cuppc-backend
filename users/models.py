from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the `Student` and `Teacher` models, handling user creation.

    Methods:
        - create_user: Creates and saves a user with the given email and password. 
          Raises a ValueError if the email is not provided.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)  # Normalize the email to lowercase
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password before saving
        user.save(using=self._db)  # Save the user in the database
        return user


class Student(AbstractBaseUser):
    """
    Model representing a student user.

    Fields:
        - full_name: The student's full name (max length: 255).
        - varsity_id: A unique identifier for students (max length: 8).
        - email: The student's unique email address.
        - password: The student's hashed password.

    Custom Manager:
        - objects: An instance of `CustomUserManager` to handle student creation.

    Authentication:
        - USERNAME_FIELD: Uses `varsity_id` as the unique identifier for login.
        - REQUIRED_FIELDS: Requires `full_name` and `email` to create a user.
    """
    full_name = models.CharField(max_length=255)
    varsity_id = models.CharField(max_length=8, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    objects = CustomUserManager()

    USERNAME_FIELD = 'varsity_id'
    REQUIRED_FIELDS = ['full_name', 'email']


def validate_teacher_email(value):
    """
    Validates that the teacher's email ends with '@physics.cu.ac.bd'.
    
    Raises:
        - ValidationError: If the email does not match the required domain.
    """
    if not value.endswith('@physics.cu.ac.bd'):
        raise ValidationError('Email must end with @physics.cu.ac.bd')


class Teacher(AbstractBaseUser):
    """
    Model representing a teacher user.

    Fields:
        - full_name: The teacher's full name (max length: 255).
        - email: The teacher's unique email address, validated to ensure it ends with
          '@physics.cu.ac.bd'.
        - password: The teacher's hashed password.

    Custom Manager:
        - objects: An instance of `CustomUserManager` to handle teacher creation.

    Authentication:
        - USERNAME_FIELD: Uses `email` as the unique identifier for login.
        - REQUIRED_FIELDS: Requires `full_name` to create a user.
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[validate_teacher_email])
    password = models.CharField(max_length=255)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']