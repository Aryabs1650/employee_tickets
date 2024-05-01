from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ticket
from .serializers import TicketSerializer

# Define a view function named ticket_list that accepts GET and POST requests
@api_view(['GET', 'POST'])
def ticket_list(request):
    # Handle GET request to retrieve all tickets
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    
    # Handle POST request to create a new ticket
    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define a view function named ticket_detail that accepts GET, PUT, and DELETE requests
@api_view(['GET', 'PUT', 'DELETE'])
def ticket_detail(request, pk):
    try:
        # Retrieve the ticket object with the specified primary key (pk)
        ticket = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        # Return a 404 Not Found response if the ticket does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Handle GET request to retrieve details of a specific ticket
    if request.method == 'GET':
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    
    # Handle PUT request to update details of a specific ticket
    elif request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Handle DELETE request to delete a specific ticket
    elif request.method == 'DELETE':
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
