from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Picture = models.ImageField(upload_to="profile_pics/")
    handle = models.CharField(
        verbose_name="handel",
        max_length=128,
        unique=True,
        validators=[
            UnicodeUsernameValidator(regex="^@",message="Handle must start with \'@\' symbol")
        ]
    )
    bio = models.TextField(max_length=100)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post {self.id} by {self.user.username}"

class Media(models.Model):
    IMAGE = 'image'
    VIDEO = 'video'
    AUDIO = 'audio'
    FILE = 'file'

    MEDIA_TYPE_CHOICES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
        (AUDIO, 'Audio'),
        (FILE, 'File'),
    ]

    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='media_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media {self.id} of type {self.media_type} for post {self.post.id}"
