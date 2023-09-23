from django import forms
from .models import NewsModel
class NewsForm(forms.ModelForm):
    name_uz = forms.CharField()
    name_ru = forms.CharField()
    name_en = forms.CharField()

    status_uz = forms.CharField
    status_ru = forms.CharField
    status_en = forms.CharField

    class Meta:
        model = NewsModel
        exclude = ('name', 'status')