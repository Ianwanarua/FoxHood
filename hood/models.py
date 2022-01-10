from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=200)
    hood_location = models.CharField(max_length=200)
    hood_description = models.TextField(max_length=500, blank=True)
    hood_photo = CloudinaryField('photo', default='photo')
    Police_Toll = models.IntegerField(null=True, blank=True)
    Hospital_Toll = models.IntegerField(null=True, blank=True)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return self.hood_name
        # return f'{self.hood_name} neighbourhood'

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

    @property
    def occupants_count(self):
        return self.neighbourhood_users.count()

    def update_hood(self):
        hood_name = self.hood_name
        self.hood_name = hood_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idNo = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
    profile_pic = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)


class Business(models.Model):
    business_name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    business_email = models.CharField(max_length=30)
    business_desc = models.TextField(blank=True)
#     business_photo = CloudinaryField('businessphoto',default='')

    def __str__(self):
        # return self.business_name
        return f'{self.business_name} business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    image = CloudinaryField('images')
    content = models.TextField(max_length=300, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, default='', null=True, blank=True)

    def __str__(self):
        return self.title

    def save_post(self):
        return self.save()

    def delete_post(self):
        self.delete()
