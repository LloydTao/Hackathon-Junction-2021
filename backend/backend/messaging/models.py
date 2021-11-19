from django.db import models
from accounts.models.user import User

# Create your models here.


class Room(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"Room: {self.name}"


class Message(models.Model):
    room = models.ForeignKey(Room, null=False, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    flags = models.IntegerField(default=0)

    def __str__(self):
        return f"Message from {self.sender.username}"
