from django.db import models
from django.utils import timezone

# Employee model to represent employees in the system
class Employee(models.Model):
    name = models.CharField(max_length=100)  # Field to store the name of the employee
    # Other employee details...  # Additional fields can be added here to store more details about the employee

# DutyRoster model to represent duty rosters for employees
class DutyRoster(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # ForeignKey to associate duty roster with an employee
    date = models.DateField()  # Field to store the date of the duty roster entry
    start_time = models.TimeField()  # Field to store the start time of the duty roster entry
    end_time = models.TimeField()  # Field to store the end time of the duty roster entry
    is_available = models.BooleanField(default=True)  # Field to indicate whether the employee is available during this time slot

# Ticket model to represent tickets reported in the system
class Ticket(models.Model):
    ticket_number = models.CharField(max_length=100)  # Field to store the ticket number
    creation_date = models.DateTimeField(default=timezone.now)  # Field to store the creation date of the ticket
    description = models.TextField()  # Field to store the description of the ticket
    resolution_end_date = models.DateTimeField(null=True, blank=True)  # Field to store the resolution end date of the ticket (nullable)
    assigned_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # ForeignKey to associate ticket with an employee for resolution
