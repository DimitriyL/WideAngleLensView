# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import json, urllib2, sys
from utils import watson, guardian

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

#list of articles' sentences' emotions and scores
def theGrandPizzah (arr):
    masterList = []
    for each in arr:
	tempDict={}

	try:
	    tempDict['textEmotion'] = watson.sentEmotion(each['text'])
       	    tempDict['title'] = each['title']
	    tempDict['titleEmotions'] = checkNullDict(watson.mainEmotion(each['title']))
        # multiplying the scores by 100 to get percentages even though we could just
        # do it in jinja yeah too late
            for i in range(len(tempDict['titleEmotions']['scores'])):
                print tempDict['titleEmotions']['scores'][i]
                tempDict['titleEmotions']['scores'][i] *= 100
                print tempDict['titleEmotions']['scores'][i]
	    masterList.append(tempDict)
	except:
	    print "Nice!"
		    
    return masterList


articleList = theGrandPizzah(guardian.headlines())
#print articleList["titleEmotions"]["scores"][0]
my_app = Flask(__name__)
searchArticleList = []

# headlines and their emotions
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

# a specific article, split into sentences and emotions
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