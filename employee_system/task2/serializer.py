from rest_framework import serializers
from .models import Employee, DutyRoster, Ticket

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name']  # Add more fields if needed

class DutyRosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyRoster
        fields = ['id', 'employee', 'date', 'start_time', 'end_time', 'is_available']  # Add more fields if needed

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'ticket_number', 'creation_date', 'description', 'resolution_end_date', 'assigned_employee']  # Add more fields if needed
