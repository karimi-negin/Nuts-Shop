from django import forms

class ProductSearchForm(forms.Form):
    search_text = forms.CharField(max_length=100, required=False, label='Search')