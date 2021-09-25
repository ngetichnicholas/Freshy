from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.validators import MaxLengthValidator,MinLengthValidator
from cloudinary.models import CloudinaryField
from django.db.models.deletion import SET_NULL,CASCADE
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

class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    message = models.TextField()

    def save_contact(self):
        self.save()

    def delete_contact(self):
        self.delete()

    def __str__(self):
        return self.name
    
    @classmethod
    def update_contact(cls, id ,name,email ,message):
        update = cls.objects.filter(id = id).update(name = name,email = email,message=message)
        return update

class Category(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
      return self.name
  
class Grocery(models.Model):
  name = models.CharField(max_length=144)
  category = models.ForeignKey(Category,on_delete=CASCADE)
  description = models.TextField()
  selling_price = models.FloatField()
  image = models.ImageField(upload_to = 'groceries')

  def save_grocery(self):
    self.save()

  def delete_grocery(self):
    self.delete()
  
  @classmethod
  def search_groceries(cls, grocery):
    return cls.objects.filter(name__icontains=grocery).all()

  def __str__(self):
      return self.name