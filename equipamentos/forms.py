from django import forms

class DateInput(forms.DateInput):
     input_type = 'date'
     

class form_data(forms.Form):
     data_sel = forms.DateField(widget=DateInput)
     

        
            
