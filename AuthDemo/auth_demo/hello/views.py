from django.shortcuts import render
from accounts import views as accounts_views
from hello import views as hello_views


# Create your views here.
def get_index(request):
    return render(request, 'index.html')
