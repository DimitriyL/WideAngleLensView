import requests, json

link = 'https://content.guardianapis.com/us?show-most-viewed=true&show-fields=bodyText&api-key=test'

#Opening user/passw from CVS to protect API token
key=""

def headlines():
   text = requests.get(link + key).json()
   text = text['response']['mostViewed']
   arr = []
   for story in text:
      arr.append({'title': story['webTitle'], 'text': story['fields']['bodyText']})
   return arr
   
