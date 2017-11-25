import requests, json, csv
import watson

#extract key
with open('cred.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
       if row[1] == "NULL":
          key = row[0]
#print key
          
#helper method
def makeRequest(link, dictName):
   #print link
   text = requests.get(link).json()
   #print text
   text = text['response'][dictName]  
   arr = []
   for story in text:
      title = story['webTitle']
      body = story['fields']['bodyText']
      emotion = watson.mainEmotion(title)
      arr.append({'title': title, 'text': body, 'emotion': emotion})
   return arr
   
#return array of dictionary containing title, body, and emotion of headline storys
def headlines():
   link = 'https://content.guardianapis.com/us?show-most-viewed=true&show-fields=bodyText&api-key=' + key
   return makeRequest(link, 'mostViewed')

#return array of dictionary containing title, body, and emotion of storys matching keyword
def search(keyword):
   link = 'https://content.guardianapis.com/search?show-fields=bodyText&api-key=' + key + '&q=' + keyword
   return makeRequest(link, 'results')


def headlineEmotions():
   link = 'https://content.guardianapis.com/us?show-most-viewed=true&show-fields=bodyText&api-key=test'
   text = requests.get(link + key).json()
   text = text['response']['mostViewed']
   arr = []
   for story in text:
      arr.append(watson.sentEmotion(story['fields']['bodyText']))
   print arr
   return arr

print headlines()[0]
print search('trump')[0]