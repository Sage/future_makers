# Translation API - https://azure.microsoft.com/en-gb/services/cognitive-services/translator-text-api/
# Example Request - http://localhost:3001/?lang=fr&text=hello

import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl
from xml.etree import ElementTree
import http.client, urllib.request, urllib.parse, json

from helpers import *

ssl._create_default_https_context = ssl._create_unverified_context

subscription_key = get_environment_variable('TRANSLATOR_TEXT_KEY')

class Handler(http.server.SimpleHTTPRequestHandler):

    __data = "";

    # This helper function formats parts of our response properly
    def write(self,text):
        self.wfile.write(str.encode(text))

    def set_headers(self):
        self.send_response(200) # 200 means everything is OK
        self.send_header('Content-type', 'text/html') #Our response contains text
        self.end_headers()
    
    def do_GET(self):
        self.set_headers()
        self.write('Translation server is listening.')
    """
    Handles the GET request, sends to translate method and returns a response formatted
    for Chatfuel
    """
    def do_POST(self):
        print('Responding to POST request')
        print(self.path)

        description = self.translate()
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

        self.wfile.write(str.encode("{\"user_id\" : \"" + self.get_param_from_url("user_id") +"\","))
        self.wfile.write(str.encode("\"bot_id\" : \"" + self.get_param_from_url("bot_id") +"\","))
        self.wfile.write(str.encode("\"module_id\" : \"" + self.get_param_from_url("module_id") +"\","))
        self.wfile.write(str.encode("\"message\" : \"" + str(description[0]['translations'][0]['text']) +"\"}"))
        return

    """
    Gets the image path from the url and makes an api request, parses
    JSON response and returns
    """
    def translate(self):
        print("We're doing translation")
        text = self.get_param_from_url("incoming_message")
        lang = "es"
        returned = self.make_api_request(text, lang)
        return returned

    """    
    Method to send an API Request to Azure 
    """
    def make_api_request(self, text, lang):

        host = 'api.cognitive.microsofttranslator.com'
        path = '/translate?api-version=3.0'

        params = '&to=' + lang

        headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type' : 'application/json'}
        conn = http.client.HTTPSConnection(host)

        body = "[{'Text':'" + text + "'}]"   #urllib.parse.quote(text)
        conn.request ("POST", path + params, body, headers)
        response = conn.getresponse ()

        data = response.read()
        parsed = json.loads(data)
        conn.close()
        return parsed

    def get_param_from_url(self, param_name):
        queryStarts = self.path.find("?") + 1
        if self.__data == "":
            self.__data = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        from urllib.parse import parse_qs
        parsed = parse_qs(self.path[queryStarts:])
        parsed = parse_qs(self.__data)
        return parsed[param_name][0]

# Get the server ready and start listening

port = 3001
httpd = socketserver.TCPServer(('', port), Handler)
print('The server is now listening on port ' + str(port) + '. Visit localhost:' + str(port) +' in your browser!')

httpd.serve_forever()
