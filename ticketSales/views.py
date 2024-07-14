from django.shortcuts import render
from django.http import HttpResponse
from ticketSales.models import ConcertModel
# Create your views here.

def consertListView(request):
    concerts=ConcertModel.objects.all()
    
    context= {
        "concertlist": concerts,
        "concertcount": concerts.count
    }
    return render(request, "ticketSales/concertlist.html", context )