from django import forms
from.models import Company, CompanyImage

# 選択フォーム(good/bad)
class ChoiceForm(forms.Form):
    data = [
        ('good', 'Good'),
        ('bad', 'Bad'),
    ]
    
    choice = forms.ChoiceField(choices=data, widget=forms.RadioSelect)

    