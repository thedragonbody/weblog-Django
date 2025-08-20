from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> welcome here! </h1>")

def home (logo):
    return HttpResponse("<h3> welcome!!! here <h3>")