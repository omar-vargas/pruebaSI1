from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
import requests 

@csrf_exempt
def create_user(request):
    if request.method == 'POST':

        
        data = json.loads(request.body)
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        tipo = data.get('tipo')
        ciudad = data.get('ciudad')
        direccion = data.get('direccion', None)
        cargo = data.get('cargo', None)
        longitude = data.get('longitude', 0)
        latitude = data.get('latitude', 0)
        geo_state = data.get('geo_state', None)

        if tipo == 'vendedor':
            if cargo not in ['asesor', 'cajero']:
                return JsonResponse({'error': 'Cargo not valid for a vendedor'}, status=400)
            direccion = None
        elif tipo == 'comprador':
            if direccion is None:
                return JsonResponse({'error': 'Direccion is mandatory for a comprador'}, status=400)
            cargo = None
        else:
            return JsonResponse({'error': 'Invalid user type'}, status=400)

        user = User(name=nombre, last_name=apellido, user_type=tipo, city=ciudad,longitude=longitude,latitude=latitude,geo_state=geo_state,
                    address=direccion, role=cargo)
        user.save()

        return JsonResponse({'message': 'User created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def update_user(request, user_id):
    # Logic to update user information
    pass



def view_user(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    if user:
        serialized_user = serializers.serialize('json', [user])
        return JsonResponse({'user': serialized_user})
    else:
        return JsonResponse({'error': 'User not found'}, status=404)


def list_users(request):
    users = User.objects.all()
    serialized_users = serializers.serialize('json', users)
    return JsonResponse({'users': serialized_users})



@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        user = User.objects.filter(pk=user_id).first()
        if user:
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        else:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# Método para geocodificar direcciones usando el servicio de Google
def geocodificar_base(request):
    # guardar el api key de Google. Podria usar variables de entorno 
    # no las uso para simplificar prueba
    api_key='AIzaSyD0txU5n7xlPZ3zkEsEjW09yVHmmEVjU4o'

    # Obtener todos los compradores sin latitud ni longitud asignadas
    users_sin_geocodificar = User.objects.filter(latitude=0.0, longitude=0.0)

    for user in users_sin_geocodificar:
        
        direccion_completa = f"{user.address}, {user.city}"  # Construir la dirección completa
        city = f"{user.city}"
        print(user.city)
       
        try:
            # Geocodificar la dirección usando el servicio de Google
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+city+'&key=AIzaSyD0txU5n7xlPZ3zkEsEjW09yVHmmEVjU4o'

            
            response = requests.get(url)
            if response.status_code == 200:
                data =  response.json()

                for resultado in data["results"]:
                    latitud = resultado["geometry"]["location"]["lat"]
                    longitud = resultado["geometry"]["location"]["lng"]
                    user.latitude= latitud
                    user.longitude = longitud
                    user.save()
                    return JsonResponse({latitud}, status=200)
            else:
                user.latitude = 0
                user.longitude = 0
                user.save()
                
            
            


        except Exception as e:
            # Manejar errores (por ejemplo, problemas de conexión o límites de la API)
            print(f"Error al geocodificar {direccion_completa}: {str(e)}")
    return JsonResponse({'usuarios': 'actualizados con geolocalizacion'}, status=200)