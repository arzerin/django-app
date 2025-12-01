from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

def home(request):
    #return HttpResponse("<h1>Welcome from FirstApp!</h1>")
    #return render(request, 'home.html')
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Success</h1>")
        

    return render (request, 'index.html', {'form' : form })


def hello_world(request):
    return HttpResponse("<h1>Hello World</h1>")

class HelloEthiopiaView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello Ethiopia</h1>")

