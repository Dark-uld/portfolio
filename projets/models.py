from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
# Create your models here.

class Projet(models.Model):
    ORIGINS = (
        ('OC', 'Openclassroom'),
        ('Perso', 'Personnel'),
        ('Pro', 'Professionnel'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    origines = models.CharField(max_length=9, choices=ORIGINS)
    tags = models.ManyToManyField('Tag', blank = True)
    url_link = models.CharField(max_length = 2000, null=True, blank=True)
    github_link = models.CharField(max_length = 2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    def __str__ (self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
class Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    alter_text = models.CharField(max_length=200)
    url_image = models.CharField(max_length = 2000, null=True, blank=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.alter_text
    
class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    skill_name = models.CharField(max_length=200)
    percentage = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    importance = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.skill_name

class Message(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        ordering = ['is_read', '-created_at']
