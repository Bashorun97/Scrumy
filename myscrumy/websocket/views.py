import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from websocket.models import Connections, ChatMessage
import boto3
# Create your views here.

@csrf_exempt
def test(request):
    return JsonResponse({'message':'hello Daud'}, status=200)

def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)

@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    connect = Connections(connection_id=connection_id)
    connect.save()
    return JsonResponse({'message':'connect successfully'}, status=200)

def disconnect(request):
    body = _parse_body(request.body)
    connection_id = body['connectionId']
    delete_id = Connections.objects.get(connection_id=connection_id)
    delete_id.delete()
    return JsonResponse({'message':'disconnected successfully'}, status=200)

def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client(
            'apigatewaymanagementapi',
            endpoint_url='https://12wpx4pa88.execute-api.us-east-2.amazonaws.com/test',
            region_name='us-east-2',
            aws_access_key_id='AKIAIWT7WQ5B5D2P5NCQ',
            aws_secret_access_key='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'
    )

    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=json.dumps(data).encode('utf-8'))

@csrf_exempt
def send_message(request):
    body = _parse_body(request.body)
    body_dict = dict(body)
    username = body_dict['body']['username']
    message = body_dict['body']['message']
    timestamp = body_dict['body']['timestamp']
    ChatMessage.objects.create(username=username, message=message, timestamp=timestamp)
    message = {
            'username' : username,
            'message' : message,
            'timestamp' : timestamp
    }

    connections = Connections.objects.all()
    data = {'messages':[message]}
    for connects in connections:
        _send_to_connection(connects.connection_id, data)
    return JsonResponse({"message":"successfully sent"}, status=200)
