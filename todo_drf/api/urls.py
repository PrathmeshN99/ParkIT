from django.urls import path
from . import views

urlpatterns = [
	path('', views.ParkingSpaceOverview, name="parking-space-overview"),
	path('parking-space-list/', views.ParkingSpaceList, name="parking-space-list"),
	path('parking-space-detail/<str:pk>/', views.ParkingSpaceDetail, name="parking-space-detail"),
	path('parking-space-create/', views.ParkingSpaceCreate, name="parking-space-create"),
	path('parking-space-update/<str:pk>/', views.ParkingSpaceUpdate, name="parking-space-update"),
	path('parking-space-delete/<str:pk>/', views.ParkingSpaceDelete, name="parking-space-delete"),
]

# Urls : 
# Register
# Login
# Home
# BookSlot
# booked/getDirections
# booked/payAmount
# EditProfile