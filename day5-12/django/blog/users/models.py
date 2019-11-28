from django.db import models
from django.contrib.auth.models import User
from PIL import Image #Use to resize image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    # RESIZE IMAGES FEARTURE, WHEN IMAGES LOCATE ON LOCAL MACHINE
    # 
    # NOW WE USE AWS S3 SO THIS WILL NOT WORK, SHOULD USE LAMBDA 
    # 
    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)

    #    # Resize image
    #    img = Image.open(self.image.path)
    #    # Max size allow 300 pixels
    #    # If image is larger we will resize it
    #    # This is just a simple way
    #    if img.height > 300 or img.width > 300:
    #        output_size = (300, 300)
    #        img.thumbnail(output_size)
    #        img.save(self.image.path)