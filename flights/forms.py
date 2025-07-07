from django import forms

class InspirationSearchForm(forms.Form):
    origin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}))
    budget = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}))
    currency = forms.CharField(max_length=3, initial='USD', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}))
    departure_date = forms.DateField(
        required=False,
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'border border-gray-300 rounded p-2 w-full'})
    )
    duration = forms.CharField(max_length=2, initial='1', widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}))

class AIInspirationSearchFrom(forms.Form):
    query = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'border border-gray-300 rounded p-2 w-full',
            'rows': 4,
            'placeholder': 'Describe your flight search...'
        }),
        help_text="e.g. Find me a flight from YYZ to anywhere under $500, leaving in August for 7 days."
    )