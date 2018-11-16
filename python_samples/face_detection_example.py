# Face Recognition API - https://azure.microsoft.com/en-gb/services/cognitive-services/face/
# Sample Image - https://how-old.net/Images/faces2/main007.jpg
# Example Request - http://localhost:3001/?image=https://how-old.net/Images/faces2/main007.jpg

import http.server
import socketserver
import urllib.parse
import urllib.request
import ssl, os
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

from helpers import *

ssl._create_default_https_context = ssl._create_unverified_context

subscription_key = get_environment_variable('FACE_RECOGNITION_KEY')

def make_api_request(params, body):
    
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


params = urllib.parse.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,facialHair,glasses,emotion,makeup,accessories',
    #'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})

target_image_url = 'https://timedotcom.files.wordpress.com/2015/01/benedict-cumberbatch.jpg'

body = "{'url': '" + target_image_url + "'}"
returned = make_api_request(params, body)
print(returned)






