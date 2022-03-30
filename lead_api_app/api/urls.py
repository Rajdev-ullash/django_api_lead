from django.urls import path, include
# from lead_api_app.api.views import lead_list,lead_details
from lead_api_app.api.views import LeadList,LeadDetails
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('list',LeadList.as_view(), name='lead-list'),
    # path('all',LeadAll.as_view(), name='lead-list'),
    path('<int:pk>', LeadDetails.as_view(), name='lead-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
