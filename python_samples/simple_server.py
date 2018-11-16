"""
Very simple HTTP (HyperText Transfer Protocol) server in Python.

This program waits for requests and replies to them with "Hello".

To test it, open a browser and enter localhost:3003 in the address bar.
localhost is the address of your local machine; 3003 is the port this
server is listening on.

"""
# First we import some libraries we need:
import http.server # Main HTTP server library
import socketserver # Another server library we need as a helper

# Now we set up a new class: our server.
class MyServer(http.server.SimpleHTTPRequestHandler):

    # We define this helper function to set the headers on our response
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
        print('Responding to GET request...')
        self._set_headers()
        self.write('Hello!')
        
# That's the end of our server class. Now we just need to make it run.
port = 3003
httpd = socketserver.TCPServer(('', port), MyServer) # Create a new server object

print('The server is now listening on port ' + str(port) + '. Visit localhost:3003 in your browser!')
httpd.serve_forever() # Start listening for requests

