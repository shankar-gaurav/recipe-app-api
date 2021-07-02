from django.db import models

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, \
                                        PermissionsMixin


#UserManager class is class that provides the helper class for creating a user or super user

class UserManager(BaseUserManager):

    #**extra_fileds --> take any of the extra arguments when you create user using 
    #this method. It makes function bit more flexible
    def create_user(self,email,password = None,**extra_fileds):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("User must have the email address")
        #**extra_fileds = pass anything extra we add

        #email=self.normalize_email(email) --> normalize_email will make sure user input email is converted into lowercase
        user = self.model(email=self.normalize_email(email),**extra_fileds)
        #this is save password in encrypted format
        user.set_password(password)

        #using=self._db --> required for supporting multiple database
        user.save(using=self._db)

        return user


    def create_superuser(self,email,password = None):
        """Creates and saves a new super user"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
        

class User(AbstractBaseUser,PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    email       = models.EmailField(max_length=255,unique=True)
    name        = models.CharField(max_length=255)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

