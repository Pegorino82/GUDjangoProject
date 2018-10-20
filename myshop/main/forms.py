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
    class Meta:
        model = MainPageContent
        fields = ['chapter', 'content', 'date', 'author']
        input_formats = ['%yyyy-%mm-%ddT%H:%M'],
        widgets = {
            # TODO  надо парсить дату/время
            'date':
                forms.widgets.DateTimeInput(
                    attrs={
                        'type': 'datetime-local',
                        'class': 'form-model-date'
                    }

            ),
        }
