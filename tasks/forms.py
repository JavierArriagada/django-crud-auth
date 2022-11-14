from django.forms import ModelForm, DateTimeField, DateTimeInput, TextInput, Textarea,  CheckboxInput
from .models import Task

# class DatePickerInput(DateTimeInput):
#  input_type = 'datetime-local'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'done', 'datecompleted']
        widgets = {
            'datecompleted': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'description': Textarea(attrs={'type': 'textarea', 'class': 'form-control'}),
            'done':  CheckboxInput(attrs={'type': 'checkbox', 'class': 'form-check-input'}),
        }

