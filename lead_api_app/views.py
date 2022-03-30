# from django.shortcuts import render
# from lead_api_app.models import Lead
# from django.http import JsonResponse
# # Create your views here.

# def lead_list(request):
#     leads=Lead.objects.all()
#     data={'leads':list(leads.values())}
#     return JsonResponse(data)

# def lead_details(request,pk):
#     leads=Lead.objects.get(pk=pk)
#     data={
#         'name':leads.name,
#         'email':leads.email,
#         'phone':leads.phone,
#         'designation':leads.designation,
#     }
#     return JsonResponse(data)