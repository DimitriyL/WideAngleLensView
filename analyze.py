import requests
from requests.auth import HTTPBasicAuth


def textToLink(text):
   return "https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&text=" + text.replace(" ", "%20")
   
def emotion(text):
   text = requests.get(textToLink(text), auth=HTTPBasicAuth('9527d887-5a97-44d6-84a9-62eb0d0631a5','aCSkCFO0dZAi')).json()
   return text

