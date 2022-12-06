from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParkingSpaceSerializer
from django.views.decorators.csrf import csrf_exempt

from .models import ParkingSpace
#########################################################################################################

@api_view(['GET'])
def ParkingSpaceOverview(request):
	api_urls = {
		'List':'/parking-space-list/',
		'Detail View':'/parking-space-detail/<str:pk>/',
		'Create':'/parking-space-create/',
		'Update':'/parking-space-update/<str:pk>/',
		'Delete':'/parking-space-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def ParkingSpaceList(request):
	spaces = ParkingSpace.objects.all().order_by('-id')
	serializer = ParkingSpaceSerializer(spaces, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ParkingSpaceDetail(request, pk):
	spaces = ParkingSpace.objects.get(id=pk)
	serializer = ParkingSpaceSerializer(spaces, many=False)
	return Response(serializer.data)


@api_view(['GET', 'POST'])
@csrf_exempt
def ParkingSpaceCreate(request):

	serializer = ParkingSpaceSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['GET', 'POST'])
@csrf_exempt
def ParkingSpaceUpdate(request, pk):
	space = ParkingSpace.objects.get(id=pk)
	serializer = ParkingSpaceSerializer(instance=space, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE','GET'])
def ParkingSpaceDelete(request, pk):
	space = ParkingSpace.objects.get(id=pk)
	space.delete()
	
	return Response('Item succsesfully deleted!')

