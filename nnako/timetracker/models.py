from django.db import models
from django.utils import timezone
from datetime import timedelta
import pytz
import random
import string

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

    PRESENCE_CHOICE = (
        ('active', 'Active'),
        ('on_leave', 'On Leave'),
        ('inactive', 'Inactive'),
    )

    EMPLOYMENT_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('remote', 'Remote'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        # Add more choices here if needed
    ]

    WORK_PREFERENCE_CHOICES = [
        ('home', 'Home'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    ]

    JOHANNESBURG_TZ = 'Africa/Johannesburg'
    TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]
    
    profile_image = models.URLField(default="https://cdn-icons-png.flaticon.com/512/6522/6522516.png")
    employee_id = models.CharField(max_length=20, unique=True)

    
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Other')  # Default to 'Other'

    date_of_birth = models.DateField(default=timezone.now)
    contact_number = models.CharField(max_length=15, default="012-345-6789")

    # insurance = models.BooleanField(choices=INSURANCE_CHOICES, default=True) 
    # address = PlainLocationField(based_fields=[name], zoom=7, default=(-26.2041, 28.0473))  # Default to Johannesburg, South Africa

    
    employment_status = models.CharField(max_length=20, choices=PRESENCE_CHOICE,default='Active')
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES, default="Gauteng")
    department = models.CharField(max_length=100, choices=DIVISION_CHOICES, default="Tech Department")
    job_title = models.CharField(max_length=100)
    employement = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES, default='full_time')
    work_preference = models.CharField(max_length=20, choices=WORK_PREFERENCE_CHOICES, default='remote')

    email = models.EmailField(unique=True)
    work_hours = models.DurationField(default=timedelta(minutes=480))

    time_zone = models.CharField(max_length=50, choices=TIMEZONE_CHOICES, default=JOHANNESBURG_TZ)
    hire_date = models.DateField()

    def generate_username(self):
        # Concatenate the first name and last name and remove spaces to create a username.
        first_name = self.name.replace(' ', '')
        last_name = self.surname.replace(' ', '')
        username = f"{first_name.lower()}_{last_name.lower()}"

        # If the generated username already exists in the database, append a random string to it.
        while Member.objects.filter(username=username).exists():
            random_suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
            username = f"{first_name.lower()}_{last_name.lower()}_{random_suffix}"

        return username

    def generate_employee_id(self):
        # Replace "COMPANYCODE" with the specific code for your company.
        company_code = "COMPANYCODE"

        # Get the highest employee ID currently in the database.
        highest_employee_id = Member.objects.order_by('-employee_id').first()

        if highest_employee_id:
            # Extract the last 4 digits of the highest employee ID and increment it.
            last_sequence_number = int(highest_employee_id.employee_id[-4:]) + 1
        else:
            # If there are no employees in the database, start with 1 as the sequence number.
            last_sequence_number = 1

        # Format the sequence number with leading zeros to have a total length of 4 digits.
        formatted_sequence_number = f"{last_sequence_number:04d}"

        # Concatenate the company code and formatted sequence number to create the employee ID.
        employee_id = f"{company_code}-{formatted_sequence_number}"
        return employee_id

    def save(self, *args, **kwargs):
        # Generate the employee ID only when creating a new member (not during updates).
        if not self.pk:
            self.employee_id = self.generate_employee_id()
        if not self.pk and not self.username:
            self.username = self.generate_username()
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


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
