# This file allows us to get rid of hand-made HTML forms
from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(max_length=7, min_length=2, error_messages={
#         "max_length": "Слишком много символов",
#         "min_length": "Слишком мало символов",
#         "required": "Укажите хотя бы один символ"
#     })
#     last_name = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 40}))
#     rating = forms.IntegerField(max_value=5, min_value=1)


# The way of creating a form based on the corresponding model
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ["name", "last_name", "feedback", "rating"]
        fields = "__all__"
        labels ={
            "name": "Имя",
            "last_name": "Фамилия",
            "feedback": "Отзыв",
            "rating": "Рейтинг",
        }
        # If we want to change the error display for every parameter we have to create those parameters as keys
        # in error_messages dictionary
        error_messages = {
            "name": {
                "max_length": "Слишком много символов",
                "min_length": "Слишком мало символов",
                "required": "Укажите хотя бы один символ"
            }
        }