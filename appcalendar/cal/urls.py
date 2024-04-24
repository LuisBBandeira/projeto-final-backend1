from django.urls import path
from .views import EventCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('events/create/', login_required(EventCreateView.as_view()), name='event_create'),
]