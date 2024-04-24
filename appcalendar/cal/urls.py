from django.urls import path
from .views import EventCreateView , EventListView , EventDetailView

urlpatterns = [
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/list/', EventListView.as_view(), name='events_list'),
    path('event/<int:event_id>/', EventDetailView.as_view(), name='event_detail'),
]