def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)
