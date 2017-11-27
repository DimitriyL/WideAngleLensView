# -*- coding: utf-8 -*-
from flask import Flask, render_template
import json, urllib2
from utils import watson, guardian

# object = urllib2.urlopen("https://content.guardianapis.com/search?api-key=b108bad9-9e7b-4afb-829b-1a9a19aef420")
# string = object.read()
# d = json.loads(string)

def checkNullDict(d):
	if len(d['tones']) == 0:
		return {'tones':'None','scores':0}
	else:
		return d

#for sentences
def addEmotionSent(arr):
	ret = []
   	for story in arr:
		story['emotion'] = watson.mainEmotion(story['text'])
	return arr

#articleList = guardian.headlines()[0]
#print articleList

'''
Return Type  
PRIMARY: LIST of DICTS
[
	{
	title: STRING
	title tones: {tones: []}
	text: string
	text emotions: [sent, emotion, score, ...]
	},
	...
]
'''
def theGrandPizzah (arr):
	masterList = []
	for each in arr:
		tempDict={}
		tempDict['title'] = each['title']
		tempDict['titleEmotions'] = checkNullDict(watson.mainEmotion(each['title']))
		tempDict['text'] = each['text']
		try:
			tempDict['textEmotion'] = watson.sentEmotion(each['text'])
		except:
			print "hmm"
		masterList.append(tempDict)

	print masterList
	return masterList

articleList = theGrandPizzah(guardian.headlines())

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template("page.html", articles = articleList)

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()