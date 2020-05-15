from django import forms
from .models import Emergency
from .models import Scheduled 
#from uploads.core.models import Emergency
import datetime

class EmergencyForm(forms.ModelForm):

    #prof = forms.ModelChoiceField(queryset=Prof.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Emergency
        fields = ['fullName', 'CSU_ID', 'startDate','reason', 'shortDesc'] 
        labels = {'startDate': 'Start Date ', 'reason' : 'Reason ',
                 'fullName' : 'Full Name ', 'CSU_ID' : 'Chico State ID # ', 
                 'shortDesc' : 'Brief summary of your situation '}
        # , 'prof'  
        # 'prof':'Professor(s) to notify:',
        #widgets = {'startDate': forms.DateInput(format=("%m/%d/%Y"))}

class ScheduledForm(forms.ModelForm):
    
    #prof = forms.ModelChoiceField(queryset=Prof.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Scheduled
        fields = ['fullName', 'CSU_ID', 'startDate', 'endDate','reason', 'shortDesc', 'Verification'] 
        labels = {'startDate': 'Start Date ', 'endDate' : 'End Date ', 'reason' : 'Reason ',
                 'fullName' : 'Full Name ', 'CSU_ID' : 'Chico State ID # ', 
                 'shortDesc' : 'Brief summary of your situation ', 'Verification' : 'Upload Supporting Documentation'}
        
        #widgets = {'startDate': forms.DateInput(format=("%m/%d/%Y"))}