from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from models import Urls
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def redireccion(request, iden):
    try:
        fila = Urls.objects.get(id=iden)
        return HttpResponseRedirect(fila.larga) 
    except Urls.DoesNotExist:
        return HttpResponseNotFound("Lo sentimos, no hay una url acortada en esta direccion")
    except ValueError:
        return HttpResponseNotFound("Value Error: Esta aplicacion acorta urls y los recursos son numeros enteros")    
    



@csrf_exempt 
def todo(request):
    salida = ""
    if request.method == "POST":
        nombre = request.POST["larga"]
        #pongo el http o https si hace falta
        if not nombre.startswith("http"):
            nombre = "http://" + nombre

        try:
            fila = Urls.objects.get(larga=nombre)
            salida += "<b>ERROR: la url '" + fila.larga + "' esta acortada ya en: " + str(fila.id) + "</b><br><br>"
        except Urls.DoesNotExist:
            salida += "Guardada correctamente la url '" + str(nombre) + "'<br><br>"
            #Guardo en la BD
            p = Urls(larga=nombre)
            p.save()
            
                           
    salida += "<form action='' method='POST'>\n"
    salida += "Url a acortar: <input type='text' name='larga'>"
    salida += '<input type="submit" value="Acortar"><br>'
    salida += "<br><hr>Estas son las urls acortadas:<ul>"
    lista = Urls.objects.all()
    for fila in lista:
        salida += "<li>" + str(fila.id) + "->" + fila.larga + " "
    salida += "</ul>"

    return HttpResponse(salida)
