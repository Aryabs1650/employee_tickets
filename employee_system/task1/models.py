from django.db import models

# Define a Django model named Ticket
class Ticket(models.Model):
    # Define a field to store the ticket number as a character string with a maximum length of 100 characters
    ticket_number = models.CharField(max_length=100)
    
    # Define a field to store the creation date and time of the ticket
    creation_date = models.DateTimeField()
    
    # Define a field to store the description of the ticket as a text field
    description = models.TextField()
    
    # Define a field to store the resolution end date and time of the ticket
    resolution_end_date = models.DateTimeField(null=True, blank=True)

