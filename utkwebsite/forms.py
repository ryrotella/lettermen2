from django.forms import ModelForm
from django.core import validators
from .models import ServiceAward, LetterAward, BoardAward
from django import forms

class ServiceForm(ModelForm):


    class Meta:
        model = ServiceAward
        fields = "__all__"
        widgets = {
            'full_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ex. Thomas Phillip Smith'
                }
            ), 
            'sport': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ex. Track and Field'
                }
            ), 
            'year': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'ex. 1998'
                }
            ),
           
            'statement': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'I support this nominee because... (feel free to copy and paste from wherever you\'ve written your statement)',
                    'cols': '69',
                    'rows': '10',
                }
            ), 
            'nominator': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Your name here'
                }
            ),   
        }
    
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['year'].required = False

class LetterForm(ModelForm):

    class Meta:
        model = LetterAward
        fields = "__all__"
        widgets = {
            'full_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ex. Thomas Phillip Smith'
                }
            ), 
            'relation': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Alumni/Employee/etc.'
                }
            ), 
           
            'statement': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'I support this nominee because... (feel free to copy and paste from wherever you\'ve written your statement)',
                    'cols': '69',
                    'rows': '10',
                }
            ), 
            'nominator': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Your name here'
                }
            ),   
        }
    
    def __init__(self, *args, **kwargs):
        super(LetterForm, self).__init__(*args, **kwargs)

class BoardForm(ModelForm):


    class Meta:
        model = BoardAward
        fields = "__all__"
        widgets = {
            'full_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ex. Thomas Phillip Smith'
                }
            ), 
            'sport': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ex. Track and Field'
                }
            ), 
            'year': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'ex. 1998'
                }
            ),
           
            'statement': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'I support this nominee because... (feel free to copy and paste from wherever you\'ve written your statement)',
                    'cols': '69',
                    'rows': '10',
                }
            ), 

            'address_one': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': '123 Easy St'

                }  
            ),

            'address_two': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Apartment, studio, or floor'

                }  
            ),
            'city': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Anytown'

                }  
            ),
            'state': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'TN'

                }  
            ),
            'zip_code': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': '37919'

                }  
            ),
            'phone': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': '(865) 555-1234'

                }  
            ),

            'nominator': forms.TextInput(
                attrs = {
                    'class': 'form-control', 
                    'placeholder': 'Your name here'
                }
            ),   
        }
    
    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields['year'].required = False
        self.fields['address_two'].required = False
