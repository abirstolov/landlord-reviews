from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'lr/index.html')

def terms(request):
    return render(request, 'lr/terms-and-conditions.htm')

def add_review(request):
    return render(request, 'lr/add-review.html')