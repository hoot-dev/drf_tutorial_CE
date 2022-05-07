from django.http import JsonResponse

import json


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}

    print(request.GET)

    try:
        data = json.loads(body)
    except:
        data = {'error': 'whoops, could not parse the JSON'}
    
    print(data.keys())

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    
    return JsonResponse(data)