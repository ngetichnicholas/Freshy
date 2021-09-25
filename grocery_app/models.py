from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.validators import MaxLengthValidator,MinLengthValidator
from cloudinary.models import CloudinaryField
from django.db.models.deletion import SET_NULL
from django.db.models.fields.files import ImageField

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    full_name = models.CharField(max_length=144,blank=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    profile_picture = ImageField(upload_to='profiles')
    phone = models.CharField(max_length=13, null=True,blank=True, validators=[MinLengthValidator(10),MaxLengthValidator(13)])

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def __str__(self):
        return self.username