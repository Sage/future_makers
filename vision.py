# Vision API - https://azure.microsoft.com/en-gb/services/cognitive-services/computer-vision/
# Sample Image - https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&h=350
# Example Request - http://localhost:3001/?image=https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&h=350

import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

ssl._create_default_https_context = ssl._create_unverified_context



class Handler(http.server.SimpleHTTPRequestHandler):

    """
    Handles the GET request, sends to vision method and returns a response formatted
    for Chatfuel
    """
    def do_GET(self):
        print(self.path)

        description = self.vision()
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(str.encode("{\"messages\" : ["))
        self.wfile.write(str.encode("{\"text\" : \" this is " + description +"\" }"))
        self.wfile.write(str.encode("]}"))
        return

    """
    Gets the image path from the url and makes an api request, parses
    JSON response and returns
    """
    def vision(self):
        print("we're doing vision checks")
        image_url = self.get_param_from_url("image")
        params = urllib.parse.urlencode({
            'visualFeatures': 'Description',
            'language': 'en',
        })
        body = "{'url':'" + image_url + "'}"
        returned = self.make_api_request(params, body)
        return returned['description']['captions'][0]['text']

    """    
    Method to send an API Request to Azure 
    """
    def make_api_request(self, params, body):
        subscription_key = 'SUBSCRIPTION_KEY'
        headers = {
         'Content-Type': 'application/json',
         'Ocp-Apim-Subscription-Key': subscription_key,
        }
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        parsed = json.loads(data)
        conn.close()
        return parsed

    def get_param_from_url(self, param_name):
        queryStarts = self.path.find("?") + 1
        from urllib.parse import parse_qs
        parsed = parse_qs(self.path[queryStarts:])
        return parsed[param_name][0]


httpd = socketserver.TCPServer(('', 3001), Handler)
httpd.serve_forever()
