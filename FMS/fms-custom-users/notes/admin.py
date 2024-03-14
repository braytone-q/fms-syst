from django.contrib import admin
from .models import NoteModel, NoteCategory

# Register your models here.

admin.site.register(NoteModel)
admin.site.register(NoteCategory)