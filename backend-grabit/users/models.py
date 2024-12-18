from django.db import models 


class User(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('USER', 'Customer'),
    ]

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('BANNED', 'Banned'),
        ('INACTIVE', 'Inactive'),
    ]

    user_id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    password_hash = models.CharField(max_length=255, null=False, blank=False)
    profile_image_url = models.URLField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    address = models.TextField(null=True, blank=True) 
    registration_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    reset_token = models.CharField(max_length=255, null=True, blank=True)
    reset_token_expiration = models.DateTimeField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    is_logged_in = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username'] 
  

    def __str__(self):
        return self.username or self.email or f"User {self.user_id}"
