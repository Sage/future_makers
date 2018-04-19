import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

ssl._create_default_https_context = ssl._create_unverified_context



class Handler(http.server.SimpleHTTPRequestHandler):

    """
    Hanldes the GET request, sends to vision method and returns a response formatted
    for Chatfuel
    """
    def do_GET(s):
        print(s.path)

        description = s.vision()
        s.send_response(200)
        s.send_header("Content-type", "text/json")
        s.end_headers()
        s.wfile.write(str.encode("{\"messages\" : ["))
        s.wfile.write(str.encode("{\"text\" : \" this is " + description +"\" }"))
        s.wfile.write(str.encode("]}"))
        return

    """
    Gets the image path from the url and makes an api requset, parses
    JSON response and returns
    """
    def vision(s):
        print("we're doing vision checks")
        image_url = s.get_param_from_url("image")
        params = urllib.parse.urlencode({
            'visualFeatures': 'Description',
            'language': 'en',
        })
        body = "{'url':'" + image_url + "'}"
        returned = s.make_api_request(params, body)
        return returned['description']['captions'][0]['text']

    """    
    Method to send an API Requset to Azure 
    """
    def make_api_request(s, params, body):
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

    def get_param_from_url(s, param_name):
        queryStarts = s.path.find("?") + 1
        from urllib.parse import parse_qs
        parsed = parse_qs(s.path[queryStarts:])
        return parsed[param_name][0]


httpd = socketserver.TCPServer(('', 3001), Handler)
httpd.serve_forever()
