import requests, json
import watson

#Opening user/passw from CVS to protect API token
key=""

def headlines():
   link = 'https://content.guardianapis.com/us?show-most-viewed=true&show-fields=bodyText&api-key=test'
   text = requests.get(link + key).json()
   text = text['response']['mostViewed']
   arr = []
   for story in text:
      arr.append({'title': story['webTitle'], 'text': story['fields']['bodyText'], 'emotion': watson.mainEmotion(story['fields']['bodyText'])})
      #yeah ik im using the title's emotions and im supposed to use the article but it gives
      #me OD errors when i use the article text idk why
   return arr

def search(keyword):
   link = 'https://content.guardianapis.com/search?show-fields=bodyText&api-key=test&q=' + keyword
   text = requests.get(link + key).json()
   text = text['response']['results']
   arr = []
   for story in text:
      arr.append({'title': story['webTitle'], 'text': story['fields']['bodyText']})
   return arr

# print headlines()[0]
# print search('trump')[0]