from django import forms
from django.forms.models import inlineformset_factory  
from .models import Modules, Course

ModuleFormset = inlineformset_factory( Course, Modules,
                                      fields=['title', 'description'],
                                      extra=2,
                                      can_delete= True)