from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time',]

        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
    def save(self, commit=True):
        event = super().save(commit=False)
        if self.request and not event.user:
            event.user = self.request.user
        if commit:
            event.save()
        return event
