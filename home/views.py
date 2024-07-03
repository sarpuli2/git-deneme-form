

# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(request):
    if request.user.is_authenticated: #if request.user.is_authenticated:
        context={
            'isim':'Sertaç',
        }
    else:
        context = {
            'isim': 'Misafir',
        }

    return render(request,"home.html",context)