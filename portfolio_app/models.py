from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AboutMe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length = 250, blank=True, null=True)
    description = models.TextField()
    birthday = models.DateField()
    website = models.CharField(max_length = 250)
    phone = models.CharField(max_length = 250)
    city = models.CharField(max_length = 250)
    age = models.IntegerField()
    degree = models.CharField(max_length = 250)
    email = models.EmailField()


    def __str__(self):
        return str(self.user)


class Level(models.Model):
    level_number= models.IntegerField()

    def __str__(self):
        return str(self.level_number)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length= 250)
    level= models.ForeignKey(Level, on_delete= models.CASCADE)

    def __str__(self):
        return self.name


class Social(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter = models.CharField(max_length = 250, blank=True, null=True)
    fb = models.CharField(max_length = 250, blank=True, null=True)
    instagram = models.CharField(max_length = 250, blank=True, null=True)
    linkedin = models.CharField(max_length = 250, blank=True, null=True)

    def __str__(self):
        return self.fb


class ProfessionalExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    start_date = models.DateField()
    end_date = models.DateField()
    city = models.CharField(max_length = 250)
    description = models.TextField(max_length = 250)

    def __str__(self):
        return self.title


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    start_date = models.DateField()
    end_date = models.DateField()
    city = models.CharField(max_length = 250)
    description = models.TextField(max_length = 250)

    def __str__(self):
        return self.title


class Summary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length = 250)
    introduction = models.TextField(max_length = 250)

    def __str__(self):
        return self.name


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return str(self.user)


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)
    description = models.TextField()

    def __str__(self):
        return str(self.user)