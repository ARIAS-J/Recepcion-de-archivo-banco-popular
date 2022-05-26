from django.shortcuts import render
from csv import reader
import os

from core.settings import BASE_DIR

# Create your views here.
def home(request):
    if request.method == "POST":
        
        file = request.POST['file']
        
        print (file)
        
    return render(request, 'app/home.html')

def upload_data(request):
    pass