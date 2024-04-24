from cal.models import Event
from django.views.generic import CreateView
from .forms import EventForm


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'cal/event_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
