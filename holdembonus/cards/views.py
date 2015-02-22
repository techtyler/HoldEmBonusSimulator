from django.shortcuts import render
from django.http import HttpResponse


def card(request, card_id='KH'):
  return render(request, 'card.html', {'card': card_id})
# Create your views here.
