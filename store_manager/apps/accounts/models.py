from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import RegexValidator, ValidationError
import phonenumbers

def validate_phone_number(value):
    try:
        phone_number = phonenumbers.parse(value, None)
        if not phonenumbers.is_valid_number(phone_number):
            raise ValidationError("Enter a valid phone number.")
    except phonenumbers.NumberParseException:
        raise ValidationError("Enter a valid phone number.")

class CustomUser(AbstractUser):
    cpf = models.CharField(
        max_length=11, 
        unique=True, 
        validators=[
            RegexValidator(regex=r'^\d{11}$', message='CPF must be 11 digits')
        ]
    )
    full_name = models.CharField(max_length=255)  # Use 'full_name' instead of 'full_Name'
    phone_number = models.CharField(
        max_length=15, 
        validators=[validate_phone_number]  # Updated to use the custom validator
    )
    
    # Address fields
    street = models.CharField(max_length=255)  
    home_number = models.CharField(max_length=10)  
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)  
    country = models.CharField(max_length=100, default='Brazil')  
    
    # Set the email field as the unique identifier for the user
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username', 'full_name', 'cpf', 'phone_number', 'street', 'home_number', 'city', 'state', 'country'] 
    
    def get_full_name(self):
        return self.full_name or self.username

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # To avoid clash with the default User model
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # To avoid clash with the default User model
        blank=True
    )