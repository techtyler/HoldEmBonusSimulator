from django.shortcuts import render
from django.http import HttpResponse


#TODO: Why is this loading templates from the /cards app index?

def index(request):
	return render(request, 'index.html')

 

def auth_view(request): #do i want this to also include a parameter or lookup page from request?
	path = request.path
	return render(request, 'auth/' + path.split('/')[-1])