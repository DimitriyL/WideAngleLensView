#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, csv
from requests.auth import HTTPBasicAuth

# link = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&text='

#Example for testing
urltext = '''
Concerned that the missile defense system designed to protect American cities is insufficient by itself to deter a North Korean attack, the Trump administration is expanding its strategy to also try to stop Pyongyang's missiles before they get far from Korean airspace.

The new approach, hinted at in an emergency request to Congress last week for $4 billion to deal with North Korea, envisions the stepped-up use of cyberweapons to interfere with the North's control systems before missiles are launched, as well as drones and fighter jets to shoot them down moments after liftoff. The missile defense network on the West Coast would be expanded for use if everything else fails.

In interviews, defense officials, along with top scientists and senior members of Congress, described the accelerated effort as a response to the unexpected progress that North Korea has made in developing intercontinental ballistic missiles capable of delivering a nuclear bomb to the continental United States.

"It is an all-out effort," said Senator Jack Reed of Rhode Island, the top Democrat on the Senate Armed Services Committee, who returned from a lengthy visit to South Korea last month convinced that the United States needed to do far more to counter North Korea. "There is a fast-emerging threat, a diminishing window, and a recognition that we can't be reliant on one solution."

For years, that single solution has been the missile batteries in Alaska and California that would target any long-range warheads fired toward the American mainland, trying to shoot them down as they re-enter the atmosphere. Such an approach, known as "hitting a bullet with a bullet," remains of dubious effectiveness, even after more than $100 billion has been spent on the effort. Antimissile batteries on ships off the Korean coast and in South Korea protect against medium-range missiles, but not those aimed at American cities.
'''

#Opening user/passw from CVS to protect API token
user=''
passw=''

with open('data/cred.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        user = row[0]
        passw = row[1]

#ret value
# ret['tones'], ret['scores']
def mainEmotion(text):
	#url = url.decode(url)
	# content = requests.get(link+url, auth=HTTPBasicAuth(user, passw)).json()
	dictionary = emotion(text)
	#print content # prints dict
	ret ={}
	tonenames = []
	tonescore = []
	for each in dictionary['document_tone']['tones']:#this is a list Watson gives you
		tonenames.append(each['tone_name'])
		tonescore.append(each['score'])
	ret['tones']=tonenames # will look something like ["Sadness", "Anger"]
	ret['scores'] = tonescore# will look something like [0.8271,0.213,0.6382]
	return ret# will look something like {["Sadness", "Anger"], 0.8271,0.213,0.6382]}

def textToLink(text):
   return "https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&text=" + text.replace(" ", "%20")
   
def emotion(text):
   text = requests.get(textToLink(text), auth=HTTPBasicAuth('9527d887-5a97-44d6-84a9-62eb0d0631a5','aCSkCFO0dZAi')).json()
   return text


'''
#Creates the dict
doc = mainEmotion(urltext)

#Test print tones from emotions
for each in doc['tones']:
	print each
for each in doc['scores']:
	print each
'''

