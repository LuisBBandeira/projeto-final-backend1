from django.shortcuts import render, get_object_or_404
from cal.models import Event
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.utils import timezone

@method_decorator(login_required, name='dispatch')
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'cal/event_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')
    
@method_decorator(login_required, name='dispatch')
class EventListView(ListView):
    model = Event
    template_name = 'cal/events_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user, start_time__date=timezone.now().date())
        return queryset

@method_decorator(login_required, name='dispatch')
class EventDetailView(DetailView):
    model = Event
    template_name = 'cal/event_detail.html'

    def get_object(self, queryset=None):
        event = get_object_or_404(Event, id=self.kwargs['event_id'], user=self.request.user)
        return event