# remote-config-simple-use
simple use of firebase remote config


# cloud functions

## create a python virtual envirenmont

first have to install python3 -venv

```
    brew install python3-venv 
```

if java not found, see this StackOverflow post https://stackoverflow.com/questions/64968851/could-not-find-tools-jar-please-check-that-library-internet-plug-ins-javaapple

then execute the following code 
```
 python3 -m venv venv
```

to actate the virtual environment
```
    source venv/bin/activate
```
in order to add new packages to our virutal environment we create a  file called requirenments.txt an execute the following command:
execute only if you see the venv prefix on the terminal.
'''
pip install -r requirenments.txt
'''
if found problem with install the package pathtools execute this command:

```
    pip install wheel
```

to run the test execute this command on terminal

```
    functions-framework --target hello_world --debug
```
to change the name you must add to the url this param: /?name=Seba

prerequisite: install gclod sdk https://cloud.google.com/sdk/docs/downloads-versioned-archives
first we have to set the project id with the follow command:
```
gcloud config set project [YOUT_PROJECT_ID]
```
then we deploy our function with this command:
(python37 is because gcloud only accept 37 version)
```
gcloud functions deploy hello_world --runtime python37 --trigger-http
```
on the option Allow unauthenticated invocations of new function [hello_world]? (y/N)?  
put y

#Secure function

first we need to import the abort lib from flask to respond with a http error

the add the if statement when some request diferent to 'POST' arrive. 
in that case we respond with the http 405 error

other thing is use a bearer token to secure the calls
we need import secrets lib and use the method secrets.token_hex(16) to generate a random token of hexa encode.
```
>>> import secrets
>>> secrets.token_hex(16)
'<TOKEN_GENERATED>'
>>> 
```

create a .env file with the follow config
```
export ACCESS_TOKEN=<TOKEN_GENERATED>
````



#deploying cloud function with envirenmont variables and other dependencies.
to use flask and secure the function we need to create to files in the hello world directory
first file is requerinments.txt and add the Flask dependency
the second file is .env.yaml and we need to add the ACCESS_TOKEN generated previosly 
all in the same directory of the function
and execute the commnad

```
gcloud functions deploy [FUNCTION_NAME] --env-vars-file .env.yaml --runtime python37 --trigger-http
```

then is important to add the .env.yaml in the ignore file.

#testing function on browser

for test on browser you must execute this command, on the console of the browser (first open the develpment tools of the browser)

```
fetch('https://us-central1-monitoring-jira.cloudfunctions.net/hello_world',{method: 'POST', headers: {'Content-Type':'application/json', 'Authorization': 'Bearer XXXXXXXXXXXX'},body:JSON.stringify({'name':'seba','lastname':'arias'})}).then(response => response.text()).then(result => console.log(result))

```
this is a javascript script.

#to allow cors request

this part of the code is for allow CORS request:
```
if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Method' : 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age':'3600'
        }
        return '',204,headers
    headers = {
        'Access-Control-Allow-Origin' : '*'
    }
```
then you must add this code on the return script

```
return f'Hello {name} {lastname}', 200, headers
```