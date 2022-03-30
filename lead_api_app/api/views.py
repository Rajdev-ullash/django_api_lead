from django.shortcuts import render
from lead_api_app.models import Lead
from lead_api_app.api.serializers import LeadSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .mypagination import CustomPagination
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
# Create your views here.

class LeadList(APIView):

    def get(self,request):
        leads = Lead.objects.all().order_by('-id')
        # pagination_class = CustomPagination()
        # paginator = Paginator(leads, 4) # Show 25 contacts per page.
        # page_number = request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)        



# class LeadAll(ListAPIView):
    
#         queryset = Lead.objects.all().order_by('-id')
#         serializer_class = LeadSerializer
        # pagination_class = CustomPagination
       

class LeadDetails(APIView):
    def get(self, request,pk):
        try:
            leads = Lead.objects.get(pk=pk)
            print(leads)

        except Lead.DoesNotExist:
            return Response({'Error': 'Lead not found'},status=status.HTTP_404_NOT_FOUND)

        serializer = LeadSerializer(leads)
        return Response(serializer.data)
    
    def put(self,request,pk):
        leads = Lead.objects.get(pk=pk)
        serializer = LeadSerializer(leads,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':serializer.data})
        else:
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,pk):
        leads = Lead.objects.get(pk=pk)
        leads.delete()
        return Response({'message':'deleted'},status=status.HTTP_204_NO_CONTENT)




# @api_view(['GET','POST'])
# def lead_list(request):
#     if request.method == 'GET':
        
    
#         leads = Lead.objects.all().order_by('-id')
#         pagination_class = CustomPagination()
#         # paginator = Paginator(leads, 4) # Show 25 contacts per page.
#         # page_number = request.GET.get('page')
#         # page_obj = paginator.get_page(page_number)
#         serializer = LeadSerializer(leads, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = LeadSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def lead_details(request,pk):
#     if request.method == 'GET':
#         try:
#             leads = Lead.objects.get(pk=pk)

#         except Lead.DoesNotExist:
#             return Response({'Error': 'Lead not found'},status=status.HTTP_404_NOT_FOUND)

#         serializer = LeadSerializer(leads)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         leads = Lead.objects.get(pk=pk)
#         serializer = LeadSerializer(leads,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         leads = Lead.objects.get(pk=pk)
#         leads.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
