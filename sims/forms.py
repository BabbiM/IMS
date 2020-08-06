from django import forms
#from .models import Snippet

class sendIncidentForm(forms.Form):
    report=forms.CharField(widget=forms.Textarea)
    #output=report

class assignIncidentForm(forms.Form):
    incidentId=forms.CharField()
    incidentCategory=forms.CharField()
    incidentStatus=forms.CharField()

#(attrs={'class': 'form-check-inline'}

#class SnippetForm(forms.ModelForm):
 #   class Meta:
 #       model=Snippet
  #      fields={'report'}