# Face Recognition API - https://azure.microsoft.com/en-gb/services/cognitive-services/face/
# Sample Image - https://how-old.net/Images/faces2/main007.jpg
# Example Request - http://localhost:3001/?image=https://how-old.net/Images/faces2/main007.jpg

import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

from helpers import *

ssl._create_default_https_context = ssl._create_unverified_context

subscription_key = get_environment_variable('FACE_RECOGNITION_KEY')

class Handler(http.server.SimpleHTTPRequestHandler):
    __data = ""

    def write(self,text):
        self.wfile.write(str.encode(text))

    def set_headers(self):
        self.send_response(200) # 200 means everything is OK
        self.send_header('Content-type', 'text/html') #Our response contains text
        self.end_headers()
    
    def do_GET(self):
        self.set_headers()
        self.write('Face detection server is listening.')

    """
    Handles the GET request, sends to vision method and returns a response formatted
    for SnatchBot
    """
    def do_POST(self):
        print(self.path)


        people = self.face_recognition()
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

        user_id = self.get_param_from_url("user_id")
        bot_id = self.get_param_from_url("bot_id")
        module_id = self.get_param_from_url("module_id")

        gender = str(people [0]['faceAttributes']['gender'])

        self.write("{\"user_id\" : \"" + user_id +"\",")
        self.write("\"bot_id\" : \"" + bot_id +"\",")
        self.write("\"module_id\" : \"" + module_id +"\",")
        self.write("\"message\" : \"" + gender +"\"}")
        return

    """
    Gets the image path from the url and makes an api request, parses
    JSON response and returns
    """
    def face_recognition(self):
        print("We're doing facial recognition")
        image_url = self.get_param_from_url("incoming_message")
        print('Processing image url ' + image_url)
        params = urllib.parse.urlencode({
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,emotion,makeup,accessories',
            #'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
        })
        body = "{'url':'" + image_url + "'}"
        returned = self.make_api_request(params, body)
        return returned

    """    
    Method to send an API Request to Azure 
    """
    def make_api_request(self, params, body):
        headers = {
         'Content-Type': 'application/json',
         'Ocp-Apim-Subscription-Key': subscription_key,
        }
        conn = http.client.HTTPSConnection('northeurope.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        parsed = json.loads(data)
        conn.close()
        return parsed

    #This function gets a parameter from the incoming request
    #The parameter is encoded in the URL of the incoming request
    def get_param_from_url(self, param_name):
        if self.__data == "":
            self.__data = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        
        from urllib.parse import parse_qs
        parsed = parse_qs(self.__data)
        return parsed[param_name][0]


# Get the server ready and start listening
port = 3001
httpd = socketserver.TCPServer(('', port), Handler)
print('The server is now listening on port ' + str(port) + '. Visit localhost:' + str(port) +' in your browser!')
httpd.serve_forever()
