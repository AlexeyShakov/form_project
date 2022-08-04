from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

# # Let's make our logic with a class way not functional
# # For working with filling and getting forms we have to declare get and/or post methods in our class
# class FeedBackView(View):
#     # Get the blank form
#     def get(self, request):
#         # Just create a blank form
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={
#             "form": form
#         })
#
#     # Filling the form and sending the results to the server
#     def post(self, request):
#         # The code below gets the blank forms and it's filled with the data from request
#         form = FeedbackForm(request.POST)
#         # So we are just checking whether the form is filled or not. If yes we make redirect, if not return the clean form
#         if form.is_valid():
#             # Getting the dictionary out of request parameters
#             form.save()
#             return HttpResponseRedirect("/done")
#         return render(request, 'feedback/feedback.html', context={"form": form})

# It has the same logic as the class with the same name above
class FeedBackView(FormView):
    # We have to point what form(form class) we use
    form_class = FeedbackForm
    # We send the data to .html as 'form' variable. If we send something else we get nothing in response!!!
    template_name = 'feedback/feedback.html'
    # We have to point where we go after our submit has been approved
    success_url = '/done'

    # This method obliges us to do something with the data from the form
    def form_valid(self, form):
        form.save()
        return super(FeedBackView, self).form_valid(form)


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


# class 'ListView' is good for displaying all data from the DB
class ListFeedBack(ListView):
    template_name = "feedback/list_feedback.html"
    model = Feedback
    # ListView put the data from the DB in the 'context' variable automatically. It creates new key for it - 'objects_list'
    # # But we can change that by setting the needed variable
    # context_object_name = "our_name"

    # This method might be needed for filtering our data from the DB
    def get_queryset(self):
        queryset = super().get_queryset()
        filtered_queryset = queryset.filter(rating__gt=4)
        return filtered_queryset


class DetailFeedBack(DetailView):
    template_name = "feedback/detail_feedback.html"
    model = Feedback
    # To use DetailView we have to point the parameter with the special name 'pk'(primary key) in urls.py
    # DetailView saves the needed data in 'context' variable with the name of the model but in lowercase. So we have to indicate this name in .html
    # # But we can change that by setting the needed variable
    # context_object_name = "our_name"


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