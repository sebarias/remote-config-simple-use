def hello_world(request):
    #request.get_json(silent=True) to get json and silent=true means if json no exist, the return is None
    request_args = request.args
    request_json = request.get_json(silent=True)

    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'world'
        lastname = ''

    return f'Hello {name} {lastname}'