from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View

# Let's make our logic with a class way not functional
class FeedBackView(View):
    # The names of methods must be the same like HTTP methods
    def get(self, request):
        # Just create a blank form
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={
            "form": form
        })

    def post(self, request):
        # The code below gets the blank forms and it's filled with the data from request
        form = FeedbackForm(request.POST)
        # So we are just checking whether the form is filled or not. If yes we make redirect, if not return the clean form
        if form.is_valid():
            # Getting the dictionary out of request parameters
            form.save()
            return HttpResponseRedirect("/done")
        return render(request, 'feedback/feedback.html', context={"form": form})


class DoneView(View):
    def get(self, request):
        return render(request, 'feedback/done.html')


class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        # Get the data from the DB with the got id
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={
            "form": form
        })

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        # By pointing "instance=feed" we say django that we wanna work with the row already exsited in the table
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/done")
        else:
            feed = Feedback.objects.get(id=id_feedback)
            form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={
            "form": form
        })

# FUNCTIONAL WAY!

# # Create your views here.
# def index(request):
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         # So we are just checking whether the form is filled or not. If yes we make redirect, if not return the clean form
#         if form.is_valid():
#             # Getting the dictionary out of request parameters
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect("/done")
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={"form": form})
#
#
#
# def done(request):
#     return render(request, 'feedback/done.html')
#
# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == "POST":
#         # By pointing "instance=feed" we say django that we wanna work with the row already exsited in the table
#         form = FeedbackForm(request.POST, instance=feed)
#         # So we are just checking whether the form is filled or not. If yes we make redirect, if not return the clean form
#         if form.is_valid():
#             # Getting the dictionary out of request parameters
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect("/done")
#     else:
#     # The code below filles the needed form with existing data from the DB
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={
#         "form": form
#     })