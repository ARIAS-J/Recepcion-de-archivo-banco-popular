import codecs
from django.shortcuts import render
from django.contrib import messages

from app.models import Empresa, Nominas

# Create your views here.
def home(request):
    if request.method == "POST":
        
        file = codecs.EncodedFile(request.FILES['file'],"UTF-8")
        
        lines = file.readlines()

        for line in lines:
            
            line = str(line).split("|")
            
            if line[0] == "b'E":
                rnc = line[1]
                numero_cuenta= line[2]
                fecha = line[3]
                
                # queryset
                Empresa.objects.create(rnc = rnc, numero_cuenta = numero_cuenta, fecha = fecha)
            elif line[0] == "b'D":
                cedula = line[1]
                nombre =line[2]
                primer_apellido = line[3]
                segundo_apellido = line[4]
                puesto = line[5]
                cuenta = line[6]
                monto = line[7][0:-3]
                
                # queryset
                Nominas.objects.create(cedula = cedula, nombre = nombre, primer_apellido = primer_apellido, segundo_apellido = segundo_apellido, puesto_trabajo = puesto, numero_cuenta = cuenta, monto_pagar = monto, empresa_rnc_id = rnc)
                
            elif line[0] == "b'S":
                registro = line[1]
        messages.success(request, "Archivo cargado con exito.")
        
    return render(request, 'app/home.html')

def upload_data(request):
    pass