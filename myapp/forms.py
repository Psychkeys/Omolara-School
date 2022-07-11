from django import forms
from newsletter.models import Subscribers


class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]

