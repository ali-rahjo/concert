from django.shortcuts import render
from django.http import HttpResponse
from ticketSales.models import concertModel
# Create your views here.

def consertListView(request):
    concerts=concertModel.objects.all()
    text= """
<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <h1>lists of concerts</h1>
        <ul>
        {}
        </ul>
    </body>
</html>
        """ .format('\n'.join('<li>{}</li>'.format(concert)  for concert in concerts))
    return HttpResponse(text)