from django.db import models
from django.contrib.auth.models import User 

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,default=None, 
                              null=True,on_delete=models.CASCADE)
    
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='p_app/profile_pic',blank=True)
    
    def __str__(self):
        return self.user.username