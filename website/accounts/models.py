from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, phone, password):
        if not username:
            raise ValueError('plz enter username')
        
        if not email:
            raise ValueError('plz enter email')
        
        if not phone:
            raise ValueError('plz enter phone')
        
        
        user = self.model(username=username, email=self.normalize_email(email), phone=phone)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, phone, password):
        user = self.create_user(username, email, phone, password)
        
        user.is_admin = True

        user.save(using=self._db)

        return user
        


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ['email', 'phone']

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
    





