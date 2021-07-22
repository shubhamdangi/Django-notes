from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

#  code to compress the profile image size Begin
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) #remember this 1.list , 2.dict
        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
#  code to compress the profile image End

