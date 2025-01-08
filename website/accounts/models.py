from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from my_plants.models import Plants

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username:
            raise ValueError('plz enter username')
        
        if not email:
            raise ValueError('plz enter email')
        
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        
        user.is_admin = True

        user.save(using=self._db)

        return user
        


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    users_plants = models.ManyToManyField(Plants, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'





