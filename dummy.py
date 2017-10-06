import requests
import json
import sys
from StringIO import StringIO
import getopt

TOKEN = '860a2e8f6b125e4c7b9bc83709a0ac1ddac9d40f'
TOKEN_NAV = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1OGRiM2I3NGI0ODRjOTIyOTVmMTE3MWUiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE0OTA3NjI2MTl9.pHVwA2u0iaVhjJ_ljU0NtFR_y0EGCwKXsLgIKSUcCK8'
NAV_API_URL = 'http://localhost:9001/api/'

it = 0

def postItinerary(itinerary):
    #print itinerary

    url_nav_itinerary = NAV_API_URL + 'itineraries/'
    response = requests.post(url_nav_itinerary, data={'refId':itinerary['id_itinerario'], 'depart':itinerary['zarpe'], 'name':itinerary['nombre_ruta'], 'active':'true'}, headers={'Authorization':'Baerer ' + TOKEN_NAV})

    itineraryObjectId = ''

    try:
        itineraryObjectId = json.loads(response.text)['_id']
    except:
        itineraryObjectId = json.loads(response.text)['op']['_id']

    return itineraryObjectId

def postPort(port):
    #print port

    url_nav_port = NAV_API_URL + 'seaports/'
    response = requests.post(url_nav_port, data={'locationId':port['id_ubicacion'], 'locationName':port['nombre_ubicacion']}, headers={'Authorization':'Baerer ' + TOKEN_NAV})

def postManifest(manifest, itineraryObjectId):
    for m in manifest:
        url_nav_manifest = NAV_API_URL + 'manifests/'
        response = requests.post(url_nav_manifest, data={'name':m['nombre_pasajero'], 'sex':m['sexo'], 'resident':m['residente'],
                                                        'nationality':m['nacionalidad'], 'documentId':m['codigo_pasajero'],
                                                        'documentType':m['nombre_cod_documento'], 'reservationId':m['id_detalle_reserva'],
                                                        'reservationStatus':m['estado_detalle_reserva'], 'ticketId':m['ticket'], 'originName':m['origen'],
                                                        'destinationName':m['destino'], 'itinerary':itineraryObjectId}, headers={'Authorization':'Baerer ' + TOKEN_NAV})

def getItineraryObjectId(mdate, itinerary_id):
    url_nav_manifest = NAV_API_URL + 'itineraries?date=' + mdate
    response = requests.get(url_nav_manifest , headers={'Authorization':'Baerer ' + TOKEN_NAV})

    itineraries = json.loads(response.text)
    for itinerary in itineraries:
        if(itinerary['refId'] == itinerary_id):
            return str(itinerary['_id'])

    return "-1"

if it == 0:
    itineraries = [
                    {'id_itinerario': 1, 'zarpe': '2016-10-10T01:00:00.000Z', 'codigo_ruta': '205', 'nombre_ruta': 'Chait\xe9n - Ayacara'}, 
                    {'id_itinerario': 2, 'zarpe': '2016-10-11T01:00:00.000Z', 'codigo_ruta': '205', 'nombre_ruta': 'Puerto Montt - Ayacara'},
                  ]
    
    
    seaports = [
                [{'nombre_ubicacion': 'Chaiten', 'id_ubicacion': 1}, {'nombre_ubicacion': 'Ayacara', 'id_ubicacion': 3}],
                [{'nombre_ubicacion': 'Puerto Montt', 'id_ubicacion': 5}, {'nombre_ubicacion': 'Ayacara', 'id_ubicacion': 3}]
               ]
    
    manifest = [
                [
                    {
                        'codigo_pasajero': '111-1', 'nombre_pasajero': 'juan perez', 'id_itinerario': 1, 
                        'nombre_cod_documento': 'C\xe9dula de Identidad', 'residente': 'No', 'id_itinerario_relacionado': None, 'sexo': 'M', 
                        'id_detalle_reserva': 11111, 'destino': 'Ayacara', 'origen': 'Chaiten', 'ticket': '111', 'nacionalidad': 'Chileno(a)', 
                        'estado_detalle_reserva': 0
                    },
                    {
                        'codigo_pasajero': '222-2', 'nombre_pasajero': 'joel san martin', 'id_itinerario': 1, 
                        'nombre_cod_documento': 'C\xe9dula de Identidad', 'residente': 'No', 'id_itinerario_relacionado': None, 'sexo': 'M', 
                        'id_detalle_reserva': 22222, 'destino': 'Ayacara', 'origen': 'Chaiten', 'ticket': '222', 'nacionalidad': 'Chileno(a)', 
                        'estado_detalle_reserva': 0
                    }
                ],
                [
                    {
                        'codigo_pasajero': '333-3', 'nombre_pasajero': 'marcel gutierrez', 'id_itinerario': 2, 
                        'nombre_cod_documento': 'C\xe9dula de Identidad', 'residente': 'No', 'id_itinerario_relacionado': None, 'sexo': 'M', 
                        'id_detalle_reserva': 33333, 'destino': 'Ayacara', 'origen': 'Puerto Montt', 'ticket': '333', 'nacionalidad': 'Chileno(a)', 
                        'estado_detalle_reserva': 0
                    },
                    {
                        'codigo_pasajero': '444-4', 'nombre_pasajero': 'marco ortega', 'id_itinerario': 2, 
                        'nombre_cod_documento': 'C\xe9dula de Identidad', 'residente': 'No', 'id_itinerario_relacionado': None, 'sexo': 'M', 
                        'id_detalle_reserva': 44444, 'destino': 'Ayacara', 'origen': 'Puerto Montt', 'ticket': '444', 'nacionalidad': 'Chileno(a)', 
                        'estado_detalle_reserva': 0
                    }
                ]
               ]
    
    for i in range(len(itineraries)):
        itineraryObjectId = postItinerary(itineraries[i])
        postPort(seaports[i][0])
        postPort(seaports[i][1])
        postManifest(manifest[i], itineraryObjectId)
    


if it == 1:
    itineraries = [
                    {'id_itinerario': 1, 'zarpe': '2016-10-10T05:00:00.000Z', 'codigo_ruta': '205', 'nombre_ruta': 'Chait\xe9n - Ayacara'},
                    {'id_itinerario': 2, 'zarpe': '2016-10-11T01:00:00.000Z', 'codigo_ruta': '205', 'nombre_ruta': 'Puerto Montt - Ayacara'},
                  ]
    
    
    seaports = [
                [{'nombre_ubicacion': 'Chaiten', 'id_ubicacion': 1}, {'nombre_ubicacion': 'Ayacara', 'id_ubicacion': 3}],
                [{'nombre_ubicacion': 'Puerto Montt', 'id_ubicacion': 5}, {'nombre_ubicacion': 'Ayacara', 'id_ubicacion': 3}]
               ]
    
    manifest = [
                [
                    {
                        'codigo_pasajero': '777-7', 'nombre_pasajero': 'user 555', 'id_itinerario': 1,
                        'nombre_cod_documento': 'C\xe9dula de Identidad', 'residente': 'No', 'id_itinerario_relacionado': None, 'sexo': 'M',
                        'id_detalle_reserva': 55555, 'destino': 'Ayacara', 'origen': 'Chaiten', 'ticket': '555', 'nacionalidad': 'Chileno(a)',
                        'estado_detalle_reserva': 0
                    }
                ],
                [
                    {
                        'codigo_pasajero': '888-8', 'nombre_pasajero': 'user 666', 'id_itinerario': 2,
                        'nombre_cod_documento': 'C\xe9dula de Identidad', 'residente': 'No', 'id_itinerario_relacionado': None, 'sexo': 'M',
                        'id_detalle_reserva': 66666, 'destino': 'Ayacara', 'origen': 'Puerto Montt', 'ticket': '666', 'nacionalidad': 'Chileno(a)',
                        'estado_detalle_reserva': 0
                    }
                ]
               ]
    
    for i in range(len(itineraries)):
        itineraryObjectId = postItinerary(itineraries[i])
        postPort(seaports[i][0])
        postPort(seaports[i][1])
        postManifest(manifest[i], itineraryObjectId)
    
