from django.contrib import admin

# Register your models here.
from .models import Projet, Image, Message, Skill

admin.site.register(Projet)
admin.site.register(Image)
admin.site.register(Message)
admin.site.register(Skill)