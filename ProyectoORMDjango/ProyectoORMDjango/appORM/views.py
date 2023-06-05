from django.conf import settings
from django.shortcuts import render,HttpResponse
from appORM.models import *
from django.http import JsonResponse
from django.db.models import Q,Sum, Max, Count, Avg
import matplotlib.pyplot as plt
import os


# Create your views here.
#consultas a realizar
#1. Cantidad de productos vendidos por Categoria
#2. Valor total de venta por producto
#3. Valor total de Venta por Categoria
#4. Promedio de Ventas por mes
#5. Máximo valor de una venta
#6. Minimo valor de una venta
#7. Cantidad mayor de un producto vendido

def grafica1(request):
    meses = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO']
    ventas = [100000,300000,500000,450000,500000]
    
    plt.title("Ventas Primer Trimestre")
    plt.xlabel('meses')
    plt.ylabel('valor ventas')
    plt.bar(meses,ventas)
    rutaImagen = os.path.join(settings.MEDIA_ROOT+ '\\' + 'grafica.png')
    plt.savefig(rutaImagen)
    
    return render(request,"graficas.html")
