import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from websocket.models import Connection, ChatMessage

# Create your views here.

@csrf_exempt
def test(request):
    return JsonResponse({'message':'hello Daud'}, status=200)

def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.load(body_unicode)

@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    return JsonResponse({'message':'connect successfully'}, status=200)

def disconnect(request):
    connection_id = body['connectionId']
    delete_id = Connection.objects.get(connection_id=connection_id)
    return JsonResponse({'message':'disconnected successfully'}, status=200)
