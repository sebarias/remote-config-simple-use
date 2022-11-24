from flask import abort

def get_bearer_token(request):
    bearer_token = request.headers.get('Authorization', None)
    if bearer_token is None:
        abort(401)
    else:
        parts = bearer_token.split()
        if len(parts) != 2:
            abort(401)
        elif parts[0] != 'Bearer':
            abort(401)
        bearer_token = parts[1]
        return bearer_token

def hello_world(request):
    import os
    #request.get_json(silent=True) to get json and silent=true means if json no exist, the return is None
    request_args = request.args
    request_json = request.get_json(silent=True)
    if request.method != 'POST':
        abort(405)
    bearer_token = get_bearer_token(request)
    
    secret_key = os.environ.get('ACCESS_TOKEN')
    print(bearer_token, secret_key)
    if bearer_token != secret_key:
        abort(401)
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