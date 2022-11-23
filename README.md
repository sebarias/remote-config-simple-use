# remote-config-simple-use
simple use of firebase remote config


# cloud functions

## create a python virtual envirenmont

first have to install python3 -venv

'''
    brew install python3-venv 
'''

if java not found, see this StackOverflow post https://stackoverflow.com/questions/64968851/could-not-find-tools-jar-please-check-that-library-internet-plug-ins-javaapple

then execute the following code 
'''
 python3 -m venv venv
'''

to actate the virtual environment
'''
    source venv/bin/activate
'''
in order to add new packages to our virutal environment we create a  file called requirenments.txt an execute the following command:
execute only if you see the venv prefix on the terminal.
'''
pip install -r requirenments.txt
'''
if found problem with install the package pathtools execute this command:

'''
    pip install wheel
'''

to run the test execute this command on terminal

'''
    functions-framework --target hello_world --debug
'''
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