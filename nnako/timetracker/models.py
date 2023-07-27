from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField

class Member(models.Model):
    INSURANCE_CHOICES = [
        (False, 'Not Insured'),
        (True, 'Insured'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    DIVISION_CHOICES = [
        ('Tech Department', 'Tech Department'),
        # Add more choices here if needed
    ]

    BRANCH_CHOICES = [
        ('Gauteng', 'Gauteng'),
        # Add more choices here if needed
    ]

    # def upload_to_image(instance, filename):
    #     return 'img/{0}/{1}'.format(instance.name, filename)

    # profile_image = models.ImageField(upload_to=upload_to_image)
    
    profile_image = models.URLField(default="https://cdn-icons-png.flaticon.com/512/6522/6522516.png")
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Other')  # Default to 'Other'

    date_of_birth = models.DateField(default=timezone.now)
    contact_number = models.CharField(max_length=15, default="012-345-6789")

    insurance = models.BooleanField(choices=INSURANCE_CHOICES, default=True) 
    # address = PlainLocationField(based_fields=[name], zoom=7, default=(-26.2041, 28.0473))  # Default to Johannesburg, South Africa

    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES, default="Gauteng")
    division = models.CharField(max_length=100, choices=DIVISION_CHOICES, default="Tech Department")
    email = models.EmailField(unique=True)




class Project(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Member, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name

class Subtask(models.Model):
    name = models.CharField(max_length=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.name
