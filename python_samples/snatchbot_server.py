# Vision API - https://azure.microsoft.com/en-gb/services/cognitive-services/computer-vision/
# Sample Image - https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&h=350
# Example Request - http://localhost:3001/?image=https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&h=350

import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl
import json
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

ssl._create_default_https_context = ssl._create_unverified_context



class Handler(http.server.SimpleHTTPRequestHandler):


    __data = "";

    """
    Handles the POST request, sends to vision method and returns a response formatted
    for SnatchBot
    """

    def _set_headers(self):
        self.send_response(200) # 200 means everything is OK
        self.send_header('Content-type', 'text/html') #Our response contains text
        self.end_headers()

    # This helper function formats parts of our response properly
    def write(self,text):
        self.wfile.write(str.encode(text))



    # This function will be called by the server when it receives a request
    # from a browser. Inside this function, we construct our response.
    def do_GET(self):
        print('Handling GET request...')
        self._set_headers()
        self.write(self.reply)
        
    def do_POST(self):
        print('Handing POST request...')
        print(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        bot_id = self.get_param_from_url("user_id")

        reply = { "message": "It's working! Your bot ID is " + bot_id}
        reply_json = json.dumps(reply)
        self.write(reply_json)

        return


    """
    Helper method to pull a param from a URL
    """
    def get_param_from_url(self, param_name):
        if self.__data == "":
            self.__data = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
        
        from urllib.parse import parse_qs
        parsed = parse_qs(self.__data)
        return parsed[param_name][0]


httpd = socketserver.TCPServer(('', 3001), Handler)
print('Server is listening...')
httpd.serve_forever()
