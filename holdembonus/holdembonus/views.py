from django.shortcuts import render
from django.http import HttpResponse


#TODO: Why is this loading templates from the /cards app index?

def index(request):
	return render(request, 'index.html')