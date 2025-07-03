from django import forms

class InspirationSearchForm(forms.Form):
    origin = forms.CharField(max_length=100)
    budget = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.CharField(max_length=3, initial='USD')
    departure_date = forms.DateField(required=False, input_formats=['%Y-%m-%d'])

