from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView

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

# We can create a class with just a GET message is more easily with TemplateView
# class ListFeedBack(TemplateView):
#     template_name = "feedback/list_feedback.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['all_feed'] = Feedback.objects.all()
#         return context



class DetailFeedBack(TemplateView):
    template_name = "feedback/detail_feedback.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["one_row"] = Feedback.objects.get(id=kwargs["id_feedback"])
        return context


# class 'ListView' is good for displaying data from the BD
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