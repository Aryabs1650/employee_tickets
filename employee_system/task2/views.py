from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ticket, Employee, DutyRoster
from rest_framework.serializers import TicketSerializer

# API view for creating a new ticket
@api_view(['POST'])
def create_ticket(request):
    # Deserialize request data using TicketSerializer
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        # If data is valid, save the ticket
        ticket = serializer.save()
        # Allocate ticket to an available employee based on duty roster
        allocate_ticket(ticket)
        # Return success response with serialized ticket data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # If data is not valid, return error response with serializer errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Function to allocate ticket to an available employee based on duty roster
def allocate_ticket(ticket):
    # Get the list of duty roster entries for the creation date of the ticket
    duty_roster_entries = DutyRoster.objects.filter(date=ticket.creation_date)
    # Filter duty roster entries to get available employees
    available_employees = duty_roster_entries.filter(is_available=True)
    if available_employees.exists():
        # Get the next available employee
        assigned_employee = available_employees.first().employee
        # Assign the ticket to the available employee
        ticket.assigned_employee = assigned_employee
        ticket.save()  # Save the ticket with assigned employee
