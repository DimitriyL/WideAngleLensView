import requests, json, csv

#extract key
if __name__ == "__main__":
   csvDataFile = open('cred.csv')
else:
   csvDataFile = open('utils/cred.csv')
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
      arr.append({'title': title, 'text': body})
   return arr
   
#return array of dictionary containing title and body of headline storys
def headlines():
   key="test"
   link = 'https://content.guardianapis.com/us?show-most-viewed=true&show-fields=bodyText&api-key=' + key
   return makeRequest(link, 'mostViewed')

#return array of dictionary containing title and body of storys matching keyword
def search(keyword):
   key="test"
   link = 'https://content.guardianapis.com/search?show-fields=bodyText&api-key=' + key + '&q=' + keyword
   return makeRequest(link, 'results')

#print headlines()[0]['text']
#print search('trump')[0]
