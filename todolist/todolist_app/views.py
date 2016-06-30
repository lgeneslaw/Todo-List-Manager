from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from todolist_app.models import Task
from todolist_app.forms import TaskForm

from datetime import datetime, date, time, timedelta

SUNDAY = 6


################################################################################################
#                                           Views                                              #
################################################################################################


# "home" view is all incomplete tasks
def index(request):
    template = loader.get_template('todolist_app/incomplete.html')
    tasks = Task.objects.all().filter(complete=False).order_by('due')
    return HttpResponse(template.render({'tasks': tasks}, request))
    

# displays one day of tasks
# Loads current day if date not specifid
def day(request, year=None, month=None, day=None):
    
    # if date not specified, load today's view
    if not (year and month and day):
        today = datetime.now()
        return redirect('day', year=str(today.year), month=str(today.month), day=str(today.day))
    
    # build context
    tasks = _getTasksByDate(year, month, day, False)
    d = date(int(year), int(month), int(day))
    weekday = d.strftime("%A")  # get weekday as string
    context = { 
        'tasks': tasks,
        'weekday': weekday,
        'date': d,
        'next_day': d + timedelta(1), # used for pagination
        'prev_day': d - timedelta(1), # used for pagination
    }
    template = loader.get_template('todolist_app/day.html')
    return HttpResponse(template.render(context, request))


# displays tasks completed on given day
# Loads current day if date not specified
def completed_day(request, year=None, month=None, day=None):
    
    # if date not specified, load today's view
    if not (year and month and day):
        today = datetime.now()
        return redirect('day', year=str(today.year), month=str(today.month), day=str(today.day))
    
    # build context
    tasks = _getTasksByDate(year, month, day, True)
    d = date(int(year), int(month), int(day))
    weekday = d.strftime("%A") # get weekday as string
    context = { 
        'tasks': tasks,
        'weekday': weekday, # show weekday name
        'date': d,
        'next_day': d + timedelta(1), # used for pagination
        'prev_day': d - timedelta(1), # used for pagination
    }
    template = loader.get_template('todolist_app/completed_day.html')
    return HttpResponse(template.render(context, request))


# displays one week of tasks, always starting on Sunday
# Loads current week if date not specified
def week(request, year=None, month=None, day=None):

    # if date not specified, load this week's view
    if not (year and month and day):
        today = datetime.now()
        return redirect('week', year=str(today.year), month=str(today.month), day=str(today.day))
    
    # if given date is midweek, redirect to start of week (Sunday)
    d = date(int(year), int(month), int(day))
    if(d.weekday() != SUNDAY):
        return _findWeekStart(d)
    
    # build week_tasks array by fetching tasks one day at a time
    week_tasks = []
    date_iter = d
    for i in range(0, 7):
        tasks = _getTasksByDate(date_iter.year, date_iter.month, date_iter.day, False)
        # do not display days with no tasks
        if(tasks):
            weekday = date_iter.strftime("%A")
            week_tasks.append(
                {
                    'weekday': weekday,
                    'year': date_iter.year,
                    'month': date_iter.month,
                    'day': date_iter.day,
                    'tasks': tasks
                }
            )
        date_iter = date_iter + timedelta(1) # next day

    context = {
        'week_tasks': week_tasks,
        'year': year,
        'month': month,
        'day': day,
        'next_week': d + timedelta(7), # used for pagination
        'prev_week': d - timedelta(7), # used for pagination

    }
    template = loader.get_template('todolist_app/week.html')
    return HttpResponse(template.render(context, request))


# used for both creating and editing tasks.
# if pk passed, dispatch to 'edit task' action. Else, dispatch to 'create task' action
def edit_task(request, pk=None):
    if pk:
        return _handleEditTaskRequest(request, pk)
    else:
        return _handleCreateTaskRequest(request)



################################################################################################
#                                     Task Editing (Ajax)                                      #
################################################################################################


# delete task and return home
def delete_task(request, pk):
    t = Task.objects.get(pk=pk)
    t.delete()
    return redirect('index')

# mark task as completed and return home
def complete_task(request, pk):
    t = Task.objects.get(pk=pk)
    t.complete=True
    t.datetime_completed = datetime.now()
    t.save()
    return redirect('index')
    


################################################################################################
#                                       Private Helpers                                        #
################################################################################################


# depending on completed flag, return tasks either due on or completed on given date
def _getTasksByDate(year, month, day, completed):
    
    # define the range of datetimes for the given day (midnight to 11:59pm)
    start = datetime(int(year), int(month), int(day), 0, 0, 0, 0)
    end =   datetime(int(year), int(month), int(day), 23, 59, 59, 9999)
    
    # fetch the tasks either due on given day or completed on given day
    if completed:
        return Task.objects.filter(complete=True, datetime_completed__gte=start, 
                                   datetime_completed__lte=end).order_by('datetime_completed')
    else:
        return Task.objects.filter(complete=False, due__gte=start, due__lte=end).order_by('due')


# redirect to the start of the given week
def _findWeekStart(date):
    delta = (date.weekday() % SUNDAY) + 1
    d = date - timedelta(delta)
    year = d.year
    month = d.month
    day = d.day
    return redirect('week', year=year, month=month, day=day)


# load the edit task form to create a new task
# return home when saved
def _handleCreateTaskRequest(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('index')
    else:
        form = TaskForm()
    template = loader.get_template('todolist_app/edit_task.html')
    return HttpResponse(template.render({'form': form, 'title': 'Create Task'}, request))


# load the edit task form to edit an existing task
# return home when saved
def _handleEditTaskRequest(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    template = loader.get_template('todolist_app/edit_task.html')
    return HttpResponse(template.render({'form': form, 'title': 'Edit Task'}, request))
