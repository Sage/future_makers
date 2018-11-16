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

subscription_key = get_environment_variable('VISION_KEY')


class Handler(http.server.SimpleHTTPRequestHandler):


    __data = "";

    # This helper function formats parts of our response properly
    def write(self,text):
        self.wfile.write(str.encode(text))

    """
    Handles the POST request, sends to vision method and returns a response formatted
    for SnatchBot
    """
    def do_POST(self):
        print('Responding to POST request...')
        print(self.path)

        description = self.vision()
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(str.encode("{\"user_id\" : \"" + self.get_param_from_url("user_id") +"\","))
        self.wfile.write(str.encode("\"bot_id\" : \"" + self.get_param_from_url("bot_id") +"\","))
        self.wfile.write(str.encode("\"module_id\" : \"" + self.get_param_from_url("module_id") +"\","))
        self.wfile.write(str.encode("\"message\" : \"" + description +"\"}"))
        return

    """
    Gets the image path from the url and makes an api request, parses
    JSON response and returns
    """
    def vision(self):
        print("we're doing vision checks")
        image_url = self.get_param_from_url("incoming_message")
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
        headers = {
         'Content-Type': 'application/json',
         'Ocp-Apim-Subscription-Key': subscription_key,
        }
        conn = http.client.HTTPSConnection('northeurope.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        parsed = json.loads(data)
        conn.close()
        return parsed

    """
    Helper method to pull a param from a URL
    """
    def get_param_from_url(self, param_name):
        if self.__data == "":
            self.__data = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        
        from urllib.parse import parse_qs
        parsed = parse_qs(self.__data)
        return parsed[param_name][0]

# Get the server ready and start listening

port = 3001
httpd = socketserver.TCPServer(('', port), Handler)
print('The server is now listening on port ' + str(port) + '. Visit localhost:3003 in your browser!')
httpd.serve_forever()
