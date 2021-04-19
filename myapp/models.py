from django.db import models


# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=200, null=True, blank=False, help_text='Enter Your Name Here')
    email = models.CharField(max_length=200, null=True, blank=False, help_text='Enter Your Email')
    phone = models.CharField(max_length=13, blank=True)
    message = models.CharField(max_length=500, null=True, blank=False)

    def __str__(self):
        return self.name
    


class Ourwork(models.Model):
    title= models.CharField(max_length=200, null=True, blank=False)
    desc = models.CharField(max_length=500, null=True, blank=False)
    image = models.ImageField(null=True, upload_to='ourwork')
    website = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Testomonial(models.Model):
    title = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, upload_to='testomonial')

    def __str__(self):
        return self.title