# This file allows us to get rid of hand-made HTML forms
from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=7, min_length=2, error_messages={
        "max_length": "Слишком много символов",
        "min_length": "Слишком мало символов",
        "required": "Укажите хотя бы один символ"
    })
    last_name = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 40}))
    rating = forms.IntegerField(max_value=5, min_value=1)