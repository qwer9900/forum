import json
from django.http import HttpResponse
from django.shortcuts import render
def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)
