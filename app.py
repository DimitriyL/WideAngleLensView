from flask import Flask, render_template
import json, urllib2
from utils import watson, guardian

# object = urllib2.urlopen("https://content.guardianapis.com/search?api-key=b108bad9-9e7b-4afb-829b-1a9a19aef420")
# string = object.read()
# d = json.loads(string)
articleList = guardian.headlines()

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template("page.html", articles = articleList)

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()