import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class NoteCategory(models.Model):
    name = models.CharField(max_length=55)


    def __str__(self):
        return self.name

class NoteModel(models.Model):
    note_owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.ForeignKey(NoteCategory, null=True, editable=True, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notes"
        ordering = ['-createdAt']

    def __str__(self) -> str:
        return self.title
