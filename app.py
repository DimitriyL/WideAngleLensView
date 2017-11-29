# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
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
            print tempDict['titleEmotions']['scores'][0]
            tempDict['titleEmotions']['scores'][0] *= 100
            print tempDict['titleEmotions']['scores'][0]
	    masterList.append(tempDict)
	except:
	    print "Nice!"
		    

    #print masterList
    return masterList


articleList = theGrandPizzah(guardian.headlines())
#print articleList["titleEmotions"]["scores"][0]
my_app = Flask(__name__)
searchArticleList = []


@my_app.route('/', methods=['GET'])
def root():
    #check query string to see if there has been a search
    keyword = request.args.get('keyword')
    #if query string is empty, display headlines
    if keyword == None:
        return render_template("base.html", articles = articleList)
    #if query string is not empty, display articles containing query
    global searchArticleList
    searchArticleList = theGrandPizzah(guardian.search(keyword))
    return render_template("base.html", articles = searchArticleList)

@my_app.route('/article' , methods=['GET', 'POST'])
def article():
    art = request.args['title']
    sent = []
    for each in articleList:
        if each['title'] == art:
	    sent = each['textEmotion']
    for each in searchArticleList:
        if each['title'] == art:
            sent = each['textEmotion']
    return render_template('article.html',sentences = sent, title= art)
    


if __name__ == "__main__":
    my_app.debug = True
    my_app.run()

