from rest_framework import serializers
from .models import Ticket

# Define a serializer class named TicketSerializer that inherits from ModelSerializer
class TicketSerializer(serializers.ModelSerializer):
    
    # Meta class to specify the model and fields to include in the serializer
    class Meta:
        # Specify the model that the serializer corresponds to
        model = Ticket
        
        # Specify the fields of the model to include in the serializer
        fields = ['id', 'ticket_number', 'creation_date', 'description', 'resolution_end_date']

