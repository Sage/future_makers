# Translation API - https://azure.microsoft.com/en-gb/services/cognitive-services/translator-text-api/
# Example Request - http://localhost:3001/?lang=fr&text=hello

import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl
from xml.etree import ElementTree
import http.client, urllib.request, urllib.parse

ssl._create_default_https_context = ssl._create_unverified_context


class Handler(http.server.SimpleHTTPRequestHandler):

    """
    Handles the GET request, sends to translate method and returns a response formatted
    for Chatfuel
    """
    def do_GET(self):
        print(self.path)

        description = self.translate()
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(str.encode("{\"messages\" : ["))
        self.wfile.write(str.encode("{\"text\" : \"" + description + "\" }"))
        self.wfile.write(str.encode("]}"))
        return

    """
    Gets the image path from the url and makes an api request, parses
    JSON response and returns
    """
    def translate(self):
        print("We're doing translation")
        text = self.get_param_from_url("text")
        lang = self.get_param_from_url("lang")
        returned = self.make_api_request(text, lang)
        return returned

    """    
    Method to send an API Request to Azure 
    """
    def make_api_request(self, text, lang):
        subscriptionKey = 'SUBSCRIPTION_KEY'

        host = 'api.microsofttranslator.com'
        path = '/V2/Http.svc/Translate'

        params = '?to=' + lang + '&text=' + urllib.parse.quote(text)

        headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
        conn = http.client.HTTPSConnection(host)
        conn.request ("GET", path + params, None, headers)
        response = conn.getresponse ()
        result = response.read()

        result = result.decode("utf-8")

        translation = ElementTree.fromstring(result).text
        return translation


    def get_param_from_url(self, param_name):
        queryStarts = self.path.find("?") + 1
        from urllib.parse import parse_qs
        parsed = parse_qs(self.path[queryStarts:])
        return parsed[param_name][0]


httpd = socketserver.TCPServer(('', 3001), Handler)
httpd.serve_forever()
