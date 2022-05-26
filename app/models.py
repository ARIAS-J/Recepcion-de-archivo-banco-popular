from django.db import models

# Create your models here.
class Empresa(models.Model):
    rnc = models.CharField(max_length=9, primary_key=True, unique=True)
    
    def __str__(self):
        return self.rnc


class Nominas(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=25)
    segundo_apellido = models.CharField(max_length=25)
    puesto_trabajo = models.CharField(max_length=50)
    numero_cuenta = models.CharField(max_length=11, unique=True)
    monto_pagar = models.FloatField(max_length=10)
    
    #Relationship
    empresa_rnc = models.ForeignKey("Empresa", on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return f"{self.cedula} {self.nombre + self.primer_apellido} {self.puesto_trabajo}"
