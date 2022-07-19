from django import forms
from .models import Task

class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget= forms.TextInput
        (attrs={'placeholder':"Enter the task's title"}))
    description = forms.CharField(max_length=150, required=False, widget= forms.Textarea
        (attrs={'placeholder':"Enter the task's description"}))
    task_due_date = forms.DateField(
        label="Select the task's due date", required=False,
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )
    task_due_time = forms.TimeField(
        label="Select the task's due time", required=False,
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )
    complete = forms.BooleanField(label='Completed this task?',
        required = False, widget=forms.widgets.CheckboxInput(attrs={'class': 'checkbox-inline'}),
    )
    
    class Meta(forms.ModelForm):
        model = Task
        fields = ('title', 'description','task_due_date','task_due_time','complete')


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget= forms.TextInput
        (attrs={'placeholder':"Enter the task's title"}))
    description = forms.CharField(max_length=150, required=False, widget= forms.Textarea
        (attrs={'placeholder':"Enter the task's description"}))
    task_due_date = forms.DateField(
        label="Select the task's due date", required=False,
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )
    task_due_time = forms.TimeField(
        label="Select the task's due time", required=False,
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )
    class Meta(forms.ModelForm):
        model = Task
        fields = ('title', 'description','task_due_date','task_due_time')
