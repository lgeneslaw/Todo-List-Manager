from django import forms
from todolist_app.models import Task
from datetimewidget.widgets import DateTimeWidget

# form used to create/edit a task. Uses a datepicker widget for the due date
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        labels = {
            'name': 'Task Name',
            'due':  'Due Date'
        }
        widgets = {'due': DateTimeWidget(usel10n=True, bootstrap_version=3)}
        fields = ('name', 'due')
