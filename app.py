
# -*- coding: utf-8 -*-
from flask import Flask, render_template
import json, urllib2, sys
from utils import watson, guardian

# object = urllib2.urlopen("https://content.guardianapis.com/search?api-key=b108bad9-9e7b-4afb-829b-1a9a19aef420")
# string = object.read()
# d = json.loads(string)

#for the unicode stuff to work in Jijna
if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')

#to make sure the dicts turn null
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
'''
Splicer: Now Useless
def splicer(s):
	s.
	ret = [] #should be # of times it runs

	bArt = len(s.encode('utf-8')) #bytes of the article
	if  bArt > 9500:
		repeatRun = bArt/9500 #how many subsections
		iterator = repeatRun
		lower = 0
		upper = len(s)/repeatRun
		print s[0:1]
		return "hi"
		while iterator > 0:
			place = s[upper:upper+1] #curr section
			while place != "." and place != "?" and place != "!":
				print upper
				print place
				print "\n\n"
				upper+=1
			ret.append(s[lower:upper])
			lower = upper
			iterator = iterator - 1
		ret.append(s[lower:len(s)-1])
		return ret
	else:
		ret.append(s)
		return ret
'''


def theGrandPizzah (arr):
	masterList = []
        #print arr
	for each in arr:
                #print each['title']
		tempDict={}

		try:
			tempDict['textEmotion'] = watson.sentEmotion(each['text'])
			tempDict['title'] = each['title']
			tempDict['titleEmotions'] = checkNullDict(watson.mainEmotion(each['title']))
			masterList.append(tempDict)
		except:
			print "Nice!"
		

	#print masterList
	return masterList

articleList = theGrandPizzah(guardian.headlines())

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template("page.html", articles = articleList)

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
