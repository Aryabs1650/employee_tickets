from django.urls import path
from . import views

# Define URL patterns for ticket-related endpoints
urlpatterns = [
    # Define URL pattern for listing all tickets and creating a new ticket
    path('', views.ticket_list),
    
    # Define URL pattern for retrieving, updating, and deleting a specific ticket
    # The <int:pk> part captures the primary key (pk) of the ticket as an integer
    path('<int:pk>/', views.ticket_detail),
]
