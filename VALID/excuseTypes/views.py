from django.shortcuts import render
from .forms import EmergencyForm,ScheduledForm
from .models import Emergency, Scheduled
 

def home(request):
    return render(request, 'excuseTypes/home.html')

def emergency(request):
    if request.method == 'POST':
        filledForm = EmergencyForm(request.POST, request.FILES)
        if filledForm.is_valid():
            filledForm.save()
            note = 'Thanks for submiting informing your professor of your %s' %(filledForm.cleaned_data['reason'])
        else:
            note: 'Form not complete, please try again' 
        newForm = EmergencyForm()
        return render(request, 'excuseTypes/emergency.html', 
                {'emergencyform':newForm, 'note':note})
    else:
        form = EmergencyForm()
        return render(request, 'excuseTypes/emergency.html', {'emergencyform':form})

def scheduled(request):
    if request.method == 'POST':
        filledForm = ScheduledForm(request.POST,request.FILES)
        if filledForm.is_valid():
            filledForm.save()
            note = 'Thanks for submiting informing your professor of your %s' %(filledForm.cleaned_data['reason'])
        else:
            note: 'Form not complete, please try again' 
        newForm = ScheduledForm()
        return render(request, 'excuseTypes/scheduled.html', {'scheduledform':newForm, 'note':note})
    else:
        form = ScheduledForm()
        return render(request, 'excuseTypes/scheduled.html', {'scheduledform':form})
