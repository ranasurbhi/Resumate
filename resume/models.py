from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Resume(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phoneno = models.CharField(max_length=15)
    summary = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Achievement(models.Model):
    resume = models.ForeignKey(Resume, related_name='achievements', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.organization}"

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='educations', on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    start_date = models.DateField()
    graduation_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} from {self.school}"

class Project(models.Model):
    resume = models.ForeignKey(Resume, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    resume = models.ForeignKey(Resume, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name