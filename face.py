# Face Recognition API - https://azure.microsoft.com/en-gb/services/cognitive-services/face/
# Sample Image - https://how-old.net/Images/faces2/main007.jpg
# Example Request - http://localhost:3001/?image=https://how-old.net/Images/faces2/main007.jpg

import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

ssl._create_default_https_context = ssl._create_unverified_context


class Handler(http.server.SimpleHTTPRequestHandler):


    __data = "";
    
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
        self.wfile.write(str.encode("{\"user_id\" : \"" + self.get_param_from_url("user_id") +"\","))
        self.wfile.write(str.encode("\"bot_id\" : \"" + self.get_param_from_url("bot_id") +"\","))
        self.wfile.write(str.encode("\"module_id\" : \"" + self.get_param_from_url("module_id") +"\","))
        self.wfile.write(str.encode("\"message\" : \"" + str(people [0]['faceAttributes']['gender']) +"\"}"))
        return

    """
    Gets the image path from the url and makes an api request, parses
    JSON response and returns
    """
    def face_recognition(self):
        print("We're doing facial recognition")
        image_url = self.get_param_from_url("incoming_message")
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
        subscription_key = 'REPLACE_WITH_KEY'
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

    def get_param_from_url(self, param_name):
        if self.__data == "":
            self.__data = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        
        from urllib.parse import parse_qs
        parsed = parse_qs(self.__data)
        return parsed[param_name][0]


httpd = socketserver.TCPServer(('', 3001), Handler)
httpd.serve_forever()
