from django import forms
from main.models import MainPageContent


class MainAuthorForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        label='Your name',
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'form-model-input',
            }
        )
    )
    lastname = forms.CharField(
        max_length=150,
        label='Your surname',
        widget=forms.widgets.TextInput(
            attrs={
                'class': 'form-model-input'
            }
        )
    )
    photo = forms.ImageField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={
                'type': 'file',
                'class': 'form-model-file'
            }
        )
    )


class MainArticleModelForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-model-date'
            }
        )
    )
    class Meta:
        model = MainPageContent
        fields = ['chapter', 'content', 'date', 'author']
        labels = {
            'date': '%Y-%m-%d %H:%M',
        }
