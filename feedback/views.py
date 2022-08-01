from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        # So we are just checking whether the form is filled or not. If yes we make redirect, if not return the clean form
        if form.is_valid():
            # Getting the dictionary out of request parameters
            print(form.cleaned_data)
            return HttpResponseRedirect("/done")
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={"form": form})



def done(request):
    return render(request, 'feedback/done.html')

