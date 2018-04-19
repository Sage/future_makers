import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

ssl._create_default_https_context = ssl._create_unverified_context



class Handler(http.server.SimpleHTTPRequestHandler):

    """
    Server GET method
    """
    def do_GET(s):
  
        return
    
    
    """    
    Method to send an API Requset to Azure 
    """
    def make_api_request(s, params, body):
        subscription_key = 'SUBSCRIPTION_KEY'
        headers = {
         'Content-Type': 'application/json',
         'Ocp-Apim-Subscription-Key': subscription_key,
        }
        #change the API URL dependent on subscription
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        parsed = json.loads(data)
        conn.close()
        return parsed


    """
    Helper method to pull a param from a URL
    """
    def get_param_from_url(s, param_name):
        queryStarts = s.path.find("?") + 1
        from urllib.parse import parse_qs
        parsed = parse_qs(s.path[queryStarts:])
        return parsed[param_name][0]


httpd = socketserver.TCPServer(('', 3001), Handler)
httpd.serve_forever()
