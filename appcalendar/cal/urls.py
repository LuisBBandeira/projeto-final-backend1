from django.urls import path
from .views import EventCreateView , EventListView , EventDetailView ,EventGlobalView ,EventDeleteView

urlpatterns = [
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/list/', EventListView.as_view(), name='events_list'),
    path('event/<int:event_id>/', EventDetailView.as_view(), name='event_detail'),
    path('events/global/', EventGlobalView.as_view(), name='event_global'),
    path('delete/<int:event_id>/', EventDeleteView.as_view(), name='event_delete'),
]