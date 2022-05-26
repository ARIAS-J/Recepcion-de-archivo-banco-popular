from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        
        file = request.FILES['file']
        print (file.read())
        
    return render(request, 'app/home.html')

def upload_data(request):
    pass